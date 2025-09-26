"""Connection management and pooling for FunASR client."""

from __future__ import annotations

import asyncio
import contextlib
import logging
import time
from typing import Any, Dict, List, Optional, Set
import weakref

from .errors import ConnectionError, ResourceExhaustedError
from .models import ClientConfig, ConnectionState
from .protocols import ReconnectingProtocol, WebSocketProtocol


class Connection:
    """Represents a single WebSocket connection to FunASR server."""

    def __init__(self, connection_id: str, protocol: WebSocketProtocol) -> None:
        """Initialize connection.

        Args:
            connection_id: Unique identifier for this connection
            protocol: WebSocket protocol instance
        """
        self.connection_id = connection_id
        self.protocol = protocol
        self.created_at = time.time()
        self.last_used_at = time.time()
        self.usage_count = 0
        self.is_busy = False
        self.session_ids: Set[str] = set()

    def mark_used(self, session_id: Optional[str] = None) -> None:
        """Mark connection as used.

        Args:
            session_id: Session ID using this connection
        """
        self.last_used_at = time.time()
        self.usage_count += 1
        if session_id:
            self.session_ids.add(session_id)

    def remove_session(self, session_id: str) -> None:
        """Remove session from this connection.

        Args:
            session_id: Session ID to remove
        """
        self.session_ids.discard(session_id)

    @property
    def idle_time(self) -> float:
        """Get idle time in seconds."""
        return time.time() - self.last_used_at

    @property
    def age(self) -> float:
        """Get connection age in seconds."""
        return time.time() - self.created_at

    @property
    def is_idle(self) -> bool:
        """Check if connection is idle."""
        return not self.is_busy and len(self.session_ids) == 0

    @property
    def is_healthy(self) -> bool:
        """Check if connection is healthy."""
        return (
            self.protocol.is_connected and self.protocol.state != ConnectionState.ERROR
        )

    def get_stats(self) -> Dict[str, Any]:
        """Get connection statistics."""
        return {
            "connection_id": self.connection_id,
            "created_at": self.created_at,
            "last_used_at": self.last_used_at,
            "usage_count": self.usage_count,
            "idle_time": self.idle_time,
            "age": self.age,
            "is_busy": self.is_busy,
            "active_sessions": len(self.session_ids),
            "protocol_stats": self.protocol.get_connection_stats(),
        }


class ConnectionPool:
    """Manages a pool of WebSocket connections to FunASR servers."""

    def __init__(
        self,
        config: ClientConfig,
        max_connections: int = 10,
        max_idle_time: float = 300.0,  # 5 minutes
        max_connection_age: float = 3600.0,  # 1 hour
        health_check_interval: float = 60.0,  # 1 minute
    ) -> None:
        """Initialize connection pool.

        Args:
            config: Client configuration
            max_connections: Maximum number of connections in pool
            max_idle_time: Maximum idle time before connection is closed
            max_connection_age: Maximum connection age before renewal
            health_check_interval: Interval for health checks
        """
        self.config = config
        self.max_connections = max_connections
        self.max_idle_time = max_idle_time
        self.max_connection_age = max_connection_age
        self.health_check_interval = health_check_interval

        self.connections: Dict[str, Connection] = {}
        self.available_connections: List[str] = []
        self.connection_counter = 0
        self.lock = asyncio.Lock()
        self.logger = logging.getLogger(__name__)

        # Background tasks
        self.health_check_task: Optional[asyncio.Task] = None
        self.cleanup_task: Optional[asyncio.Task] = None
        self._shutdown = False

        # Statistics
        self.total_connections_created = 0
        self.total_connections_closed = 0
        self.connection_reuse_count = 0

    async def start(self) -> None:
        """Start the connection pool and background tasks."""
        if not self._shutdown:
            self.health_check_task = asyncio.create_task(self._health_check_loop())
            self.cleanup_task = asyncio.create_task(self._cleanup_loop())
            self.logger.info("Connection pool started")

    async def stop(self) -> None:
        """Stop the connection pool and close all connections."""
        self._shutdown = True

        # Cancel background tasks
        if self.health_check_task:
            self.health_check_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self.health_check_task

        if self.cleanup_task:
            self.cleanup_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self.cleanup_task

        # Close all connections
        async with self.lock:
            for connection in list(self.connections.values()):
                await self._close_connection(connection)

        self.logger.info("Connection pool stopped")

    async def get_connection(self, session_id: Optional[str] = None) -> Connection:
        """Get a connection from the pool.

        Args:
            session_id: Session ID requesting the connection

        Returns:
            Available connection from pool

        Raises:
            ResourceExhaustedError: If no connections are available
            ConnectionError: If unable to create new connection
        """
        async with self.lock:
            # Try to reuse an available connection
            connection = await self._get_available_connection()

            if connection:
                connection.mark_used(session_id)
                self.connection_reuse_count += 1
                self.logger.debug(f"Reusing connection {connection.connection_id}")
                return connection

            # Create new connection if pool is not full
            if len(self.connections) < self.max_connections:
                connection = await self._create_connection()
                connection.mark_used(session_id)
                self.logger.debug(f"Created new connection {connection.connection_id}")
                return connection

            # Pool is full - try to find an idle connection to close and replace
            idle_connection = self._find_idle_connection()
            if idle_connection:
                await self._close_connection(idle_connection)
                connection = await self._create_connection()
                connection.mark_used(session_id)
                self.logger.debug(
                    f"Replaced idle connection with new connection {connection.connection_id}"
                )
                return connection

            # No connections available
            raise ResourceExhaustedError(
                "connection_pool", details={"max_connections": self.max_connections}
            )

    async def return_connection(
        self, connection: Connection, session_id: Optional[str] = None
    ) -> None:
        """Return a connection to the pool.

        Args:
            connection: Connection to return
            session_id: Session ID that was using the connection
        """
        async with self.lock:
            if connection.connection_id not in self.connections:
                return  # Connection was already removed

            if session_id:
                connection.remove_session(session_id)

            connection.is_busy = False

            # Make connection available if it's healthy
            if (
                connection.is_healthy
                and connection.connection_id not in self.available_connections
            ):
                self.available_connections.append(connection.connection_id)

            self.logger.debug(f"Returned connection {connection.connection_id} to pool")

    async def remove_connection(self, connection: Connection) -> None:
        """Remove a connection from the pool.

        Args:
            connection: Connection to remove
        """
        async with self.lock:
            if connection.connection_id in self.connections:
                await self._close_connection(connection)
                self.logger.debug(
                    f"Removed connection {connection.connection_id} from pool"
                )

    async def _get_available_connection(self) -> Optional[Connection]:
        """Get an available connection from the pool.

        Returns:
            Available connection or None if none available
        """
        while self.available_connections:
            connection_id = self.available_connections.pop(0)
            connection = self.connections.get(connection_id)

            if not connection or not connection.is_healthy:
                # Connection is unhealthy, remove it
                if connection:
                    await self._close_connection(connection)
                continue

            # Check if connection is too old
            if connection.age > self.max_connection_age:
                await self._close_connection(connection)
                continue

            connection.is_busy = True
            return connection

        return None

    async def _create_connection(self) -> Connection:
        """Create a new connection.

        Returns:
            New connection instance

        Raises:
            ConnectionError: If connection creation fails
        """
        self.connection_counter += 1
        connection_id = f"conn_{self.connection_counter}"

        try:
            # Create protocol with reconnection support if configured
            ws_kwargs = {
                "timeout": self.config.timeout,
                "ping_interval": self.config.ping_interval,
                "ping_timeout": self.config.ping_timeout,
                "close_timeout": self.config.close_timeout,
                "max_size": self.config.max_message_size,
                "compression": self.config.compression,
                "subprotocols": self.config.subprotocols,
            }

            if self.config.auto_reconnect:
                reconn = ReconnectingProtocol(
                    self.config.server_url,
                    max_retries=self.config.max_retries,
                    base_delay=self.config.retry_delay,
                    **ws_kwargs,
                )
                protocol = await reconn.connect()
            else:
                protocol = WebSocketProtocol(
                    self.config.server_url,
                    **ws_kwargs,
                )
                await protocol.connect()

            connection = Connection(connection_id, protocol)
            connection.is_busy = True

            self.connections[connection_id] = connection
            self.total_connections_created += 1

            return connection

        except Exception as e:
            self.logger.error(f"Failed to create connection {connection_id}: {e}")
            raise ConnectionError(f"Failed to create connection: {e}") from e

    async def _close_connection(self, connection: Connection) -> None:
        """Close and remove a connection.

        Args:
            connection: Connection to close
        """
        try:
            await connection.protocol.disconnect()
        except Exception as e:
            self.logger.warning(
                f"Error closing connection {connection.connection_id}: {e}"
            )

        # Remove from pool
        self.connections.pop(connection.connection_id, None)
        if connection.connection_id in self.available_connections:
            self.available_connections.remove(connection.connection_id)

        self.total_connections_closed += 1

    def _find_idle_connection(self) -> Optional[Connection]:
        """Find an idle connection that can be closed.

        Returns:
            Idle connection or None if none found
        """
        for connection in self.connections.values():
            if connection.is_idle and connection.idle_time > self.max_idle_time:
                return connection
        return None

    async def _health_check_loop(self) -> None:
        """Background task for health checking connections."""
        while not self._shutdown:
            try:
                await asyncio.sleep(self.health_check_interval)
                await self._check_connection_health()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Health check error: {e}")

    async def _check_connection_health(self) -> None:
        """Check health of all connections."""
        async with self.lock:
            unhealthy_connections = []

            for connection in self.connections.values():
                if not connection.is_healthy:
                    unhealthy_connections.append(connection)

            # Remove unhealthy connections
            for connection in unhealthy_connections:
                await self._close_connection(connection)
                self.logger.info(
                    f"Removed unhealthy connection {connection.connection_id}"
                )

    async def _cleanup_loop(self) -> None:
        """Background task for cleaning up old connections."""
        while not self._shutdown:
            try:
                await asyncio.sleep(self.health_check_interval * 2)
                await self._cleanup_old_connections()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Cleanup error: {e}")

    async def _cleanup_old_connections(self) -> None:
        """Clean up old and idle connections."""
        async with self.lock:
            connections_to_close = []

            for connection in self.connections.values():
                # Close connections that are too old or have been idle too long
                if connection.age > self.max_connection_age or (
                    connection.is_idle and connection.idle_time > self.max_idle_time
                ):
                    connections_to_close.append(connection)

            # Close old connections
            for connection in connections_to_close:
                await self._close_connection(connection)
                self.logger.debug(
                    f"Cleaned up connection {connection.connection_id} "
                    f"(age: {connection.age:.1f}s, idle: {connection.idle_time:.1f}s)"
                )

    def get_pool_stats(self) -> Dict[str, Any]:
        """Get connection pool statistics.

        Returns:
            Dictionary with pool statistics
        """
        active_connections = sum(1 for c in self.connections.values() if c.is_busy)
        idle_connections = sum(1 for c in self.connections.values() if c.is_idle)
        unhealthy_connections = sum(
            1 for c in self.connections.values() if not c.is_healthy
        )

        return {
            "total_connections": len(self.connections),
            "active_connections": active_connections,
            "idle_connections": idle_connections,
            "available_connections": len(self.available_connections),
            "unhealthy_connections": unhealthy_connections,
            "max_connections": self.max_connections,
            "utilization": len(self.connections) / self.max_connections * 100,
            "total_created": self.total_connections_created,
            "total_closed": self.total_connections_closed,
            "reuse_count": self.connection_reuse_count,
            "connection_details": [c.get_stats() for c in self.connections.values()],
        }


class ConnectionManager:
    """High-level connection manager that provides connection services."""

    def __init__(self, config: ClientConfig) -> None:
        """Initialize connection manager.

        Args:
            config: Client configuration
        """
        self.config = config
        self.pool = ConnectionPool(
            config,
            max_connections=config.connection_pool_size,
        )
        self.logger = logging.getLogger(__name__)
        self._weak_refs: Set[weakref.ReferenceType] = set()

    async def start(self) -> None:
        """Start the connection manager."""
        await self.pool.start()
        self.logger.info("Connection manager started")

    async def stop(self) -> None:
        """Stop the connection manager."""
        await self.pool.stop()
        self.logger.info("Connection manager stopped")

    async def acquire_connection(self, session_id: Optional[str] = None) -> Connection:
        """Acquire a connection from the pool.

        Args:
            session_id: Session ID requesting the connection

        Returns:
            Available connection

        Raises:
            ResourceExhaustedError: If no connections are available
            ConnectionError: If unable to create new connection
        """
        connection = await self.pool.get_connection(session_id)

        # Track connection with weak reference for automatic cleanup
        weak_ref = weakref.ref(connection, self._connection_cleanup_callback)
        self._weak_refs.add(weak_ref)

        return connection

    async def release_connection(
        self, connection: Connection, session_id: Optional[str] = None
    ) -> None:
        """Release a connection back to the pool.

        Args:
            connection: Connection to release
            session_id: Session ID that was using the connection
        """
        await self.pool.return_connection(connection, session_id)

    async def remove_connection(self, connection: Connection) -> None:
        """Remove a connection from the pool.

        Args:
            connection: Connection to remove
        """
        await self.pool.remove_connection(connection)

    def _connection_cleanup_callback(self, weak_ref: weakref.ReferenceType) -> None:
        """Callback for connection garbage collection.

        Args:
            weak_ref: Weak reference to cleaned up connection
        """
        self._weak_refs.discard(weak_ref)

    def get_stats(self) -> Dict[str, Any]:
        """Get connection manager statistics.

        Returns:
            Dictionary with manager statistics
        """
        stats = self.pool.get_pool_stats()
        stats.update(
            {
                "manager": {
                    "tracked_connections": len(self._weak_refs),
                    "config": {
                        "server_url": self.config.server_url,
                        "timeout": self.config.timeout,
                        "auto_reconnect": self.config.auto_reconnect,
                        "max_retries": self.config.max_retries,
                    },
                }
            }
        )
        return stats
