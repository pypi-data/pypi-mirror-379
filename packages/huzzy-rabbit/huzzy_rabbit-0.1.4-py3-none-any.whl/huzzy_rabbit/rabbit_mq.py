import asyncio
import json
import logging
import signal
import weakref
from typing import Any, Callable, Dict, Optional, Tuple, TypedDict, Union

from aio_pika import DeliveryMode, ExchangeType, Message, connect_robust
from aio_pika.abc import AbstractChannel, AbstractExchange, AbstractRobustConnection
from aio_pika.exceptions import AMQPConnectionError, ChannelClosed

# Type definitions for better clarity
LoopInfo = Dict[
    str,
    Union[
        AbstractRobustConnection,
        AbstractChannel,
        Dict[str, AbstractExchange],
        bool,
        None,
    ],
]


# More specific type for loop info structure
class LoopInfoDict(TypedDict):
    connection: Optional[AbstractRobustConnection]
    channel: Optional[AbstractChannel]
    exchanges: Dict[str, AbstractExchange]
    is_connecting: bool


class RabbitMQ:
    # Use weak references to track event loops and their connections
    _event_loop_connections: Dict[Any, LoopInfoDict] = weakref.WeakKeyDictionary()
    connection_url: Optional[str] = None
    reconnect_interval: int = 5  # seconds
    logger: logging.Logger = logging.getLogger(__name__)

    @staticmethod
    def _get_current_loop_info() -> (
        Tuple[Optional[asyncio.AbstractEventLoop], Optional[LoopInfoDict]]
    ):
        """Get current event loop and its connection info"""
        try:
            loop = asyncio.get_running_loop()
            if loop.is_closed():
                return None, None
            return loop, RabbitMQ._event_loop_connections.get(loop)
        except RuntimeError:
            return None, None

    @staticmethod
    def _setup_loop_cleanup(
        loop: asyncio.AbstractEventLoop, loop_info: LoopInfoDict
    ) -> None:
        """Set up cleanup handlers for the event loop"""

        def cleanup() -> None:
            if loop_info["channel"] and not loop_info["channel"].is_closed:
                asyncio.create_task(loop_info["channel"].close())
            if loop_info["connection"] and not loop_info["connection"].is_closed:
                asyncio.create_task(loop_info["connection"].close())

        try:
            loop.add_signal_handler(signal.SIGTERM, cleanup)
            loop.add_signal_handler(signal.SIGINT, cleanup)
        except (NotImplementedError, OSError):
            # Signal handlers not supported on this platform
            pass

    @staticmethod
    async def connect(connection_url: str, max_retries: int = 3) -> None:
        """Initialize connection with retry logic"""
        RabbitMQ.connection_url = connection_url
        retries = 0
        while retries < max_retries:
            try:
                await RabbitMQ._connect()
                return
            except AMQPConnectionError as e:
                retries += 1
                RabbitMQ.logger.error(
                    f"Connection attempt {retries}/{max_retries} failed: {str(e)}"
                )
                if retries == max_retries:
                    raise Exception("Max connection retries reached")
                await asyncio.sleep(RabbitMQ.reconnect_interval)

    @staticmethod
    async def _connect() -> None:
        """Internal connection method"""
        loop, loop_info = RabbitMQ._get_current_loop_info()
        if not loop or not loop_info:
            raise RuntimeError("No active event loop available")

        if loop_info["is_connecting"]:
            return

        try:
            loop_info["is_connecting"] = True
            loop_info["connection"] = await connect_robust(
                RabbitMQ.connection_url, reconnect_interval=RabbitMQ.reconnect_interval
            )
            loop_info["channel"] = await loop_info["connection"].channel()
            await loop_info["channel"].set_qos(prefetch_count=1)

            # Set up cleanup handlers
            RabbitMQ._setup_loop_cleanup(loop, loop_info)

            # Re-declare exchanges after reconnection
            for exchange_name in list(loop_info["exchanges"].keys()):
                await RabbitMQ.declare_exchange(exchange_name)
        finally:
            loop_info["is_connecting"] = False

    @staticmethod
    async def ensure_connection() -> None:
        """Ensure connection is active, reconnect if needed"""
        loop, loop_info = RabbitMQ._get_current_loop_info()
        if not loop:
            raise RuntimeError("No active event loop available")

        if not loop_info:
            # First time using this event loop
            loop_info = {
                "connection": None,
                "channel": None,
                "exchanges": {},
                "is_connecting": False,
            }
            RabbitMQ._event_loop_connections[loop] = loop_info

        if not loop_info["connection"] or loop_info["connection"].is_closed:
            await RabbitMQ._connect()
        elif not loop_info["channel"] or loop_info["channel"].is_closed:
            loop_info["channel"] = await loop_info["connection"].channel()
            await loop_info["channel"].set_qos(prefetch_count=1)

    @staticmethod
    async def publish(
        message_dict: Dict[str, Any],
        exchange_name: str,
        routing_key: str,
        message: Optional[Message] = None,
        routing_action: Optional[str] = None,
    ) -> None:
        """Publish message with connection handling"""
        try:
            await RabbitMQ.ensure_connection()
        except RuntimeError as e:
            if "No active event loop" in str(e):
                RabbitMQ.logger.warning(
                    "Event loop closed, message publishing skipped. "
                    "Consider implementing a message queue fallback."
                )
                raise ConnectionError(
                    "RabbitMQ connection unavailable due to event loop closure"
                )
            raise

        _, loop_info = RabbitMQ._get_current_loop_info()
        if not loop_info:
            raise RuntimeError("No active event loop available")

        if message is None:
            message_body = json.dumps(message_dict).encode()
            message = Message(
                message_body,
                delivery_mode=DeliveryMode.PERSISTENT,
            )

        try:
            exchange: AbstractExchange = loop_info["exchanges"][exchange_name]
        except KeyError:
            raise Exception(f"Exchange {exchange_name} not found")

        message.headers = {"action": routing_action} if routing_action else {}

        try:
            await exchange.publish(message, routing_key=routing_key)
        except (ChannelClosed, AMQPConnectionError):
            RabbitMQ.logger.warning(
                "Channel closed during publish, attempting reconnect"
            )
            await RabbitMQ.ensure_connection()
            loop, loop_info = RabbitMQ._get_current_loop_info()
            exchange = loop_info["exchanges"][exchange_name]
            await exchange.publish(message, routing_key=routing_key)

    @staticmethod
    async def declare_exchange(exchange_name: str) -> AbstractExchange:
        """Declare exchange with connection handling"""
        await RabbitMQ.ensure_connection()

        _, loop_info = RabbitMQ._get_current_loop_info()
        if not loop_info:
            raise RuntimeError("No active event loop available")

        exchange = await loop_info["channel"].declare_exchange(
            exchange_name,
            type=ExchangeType.DIRECT,
            durable=True,
        )
        loop_info["exchanges"][exchange_name] = exchange
        return exchange

    @staticmethod
    async def declare_queue_and_bind(
        queue_name: str,
        exchange_name: str,
        app_listener: Callable[[Any], Any],
        routing_key: Optional[str] = None,
    ) -> None:
        """Declare queue and bind with connection handling"""
        await RabbitMQ.ensure_connection()

        _, loop_info = RabbitMQ._get_current_loop_info()
        if not loop_info:
            raise RuntimeError("No active event loop available")

        queue = await loop_info["channel"].declare_queue(queue_name, durable=True)

        try:
            exchange: AbstractExchange = loop_info["exchanges"][exchange_name]
        except KeyError:
            raise Exception(f"Exchange {exchange_name} not found")

        routing_key = routing_key if routing_key else queue_name

        # Binding the queue to the exchange
        await queue.bind(exchange, routing_key)
        await queue.consume(app_listener)

    @staticmethod
    async def declare_queue(
        queue_name: str, exchange_name: str, routing_key: Optional[str] = None
    ) -> None:
        """Declare queue with connection handling"""
        await RabbitMQ.ensure_connection()

        _, loop_info = RabbitMQ._get_current_loop_info()
        if not loop_info:
            raise RuntimeError("No active event loop available")

        queue = await loop_info["channel"].declare_queue(queue_name, durable=True)

        try:
            exchange: AbstractExchange = loop_info["exchanges"][exchange_name]
        except KeyError:
            raise Exception(f"Exchange {exchange_name} not found")

        routing_key = routing_key if routing_key else queue_name
        await queue.bind(exchange, routing_key)

    @staticmethod
    async def remote_procedure_call(
        queue_name: str,
        on_response: Callable[[Any], Any],
        correlation_id: str,
        message_dict: Dict[str, Any],
    ) -> None:
        """Handle RPC with connection handling"""
        await RabbitMQ.ensure_connection()

        _, loop_info = RabbitMQ._get_current_loop_info()
        if not loop_info:
            raise RuntimeError("No active event loop available")

        message_body = json.dumps(message_dict).encode()
        queue = await loop_info["channel"].declare_queue(queue_name, durable=True)
        message = Message(
            message_body,
            delivery_mode=DeliveryMode.PERSISTENT,
            correlation_id=correlation_id,
            reply_to=queue.name,
        )

        try:
            await RabbitMQ.publish(
                message=message,
                routing_key="rpc_queue",
                exchange_name="rpc_exchange",
                message_dict=message_dict,
            )
            await queue.consume(on_response, no_ack=True)
        except (ChannelClosed, AMQPConnectionError):
            RabbitMQ.logger.warning("Connection lost during RPC, attempting reconnect")
            await RabbitMQ.ensure_connection()
            loop, loop_info = RabbitMQ._get_current_loop_info()
            queue = await loop_info["channel"].declare_queue(queue_name, durable=True)
            await RabbitMQ.publish(
                message=message,
                routing_key="rpc_queue",
                exchange_name="rpc_exchange",
                message_dict=message_dict,
            )
            await queue.consume(on_response, no_ack=True)

    @staticmethod
    async def close() -> None:
        """Clean up connection for current event loop"""
        _, loop_info = RabbitMQ._get_current_loop_info()
        if not loop_info:
            return

        if loop_info["channel"] and not loop_info["channel"].is_closed:
            await loop_info["channel"].close()
        if loop_info["connection"] and not loop_info["connection"].is_closed:
            await loop_info["connection"].close()

    @staticmethod
    async def close_all() -> None:
        """Clean up all connections for all event loops"""
        for _, loop_info in RabbitMQ._event_loop_connections.items():
            if loop_info["channel"] and not loop_info["channel"].is_closed:
                await loop_info["channel"].close()
            if loop_info["connection"] and not loop_info["connection"].is_closed:
                await loop_info["connection"].close()
        RabbitMQ._event_loop_connections.clear()
