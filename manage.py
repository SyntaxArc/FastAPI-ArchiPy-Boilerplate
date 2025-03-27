import asyncio
import logging

import uvicorn
from archipy.adapters.orm.sqlalchemy.adapters import AsyncSqlAlchemyAdapter
from archipy.helpers.utils.app_utils import AppUtils
from archipy.models.entities import BaseEntity
from fastapi import FastAPI

from src.configs.containers import ServiceContainer
from src.configs.dispatcher import set_dispatch_routes
from src.configs.runtime_config import RuntimeConfig

container: ServiceContainer = ServiceContainer()
container.wire(packages=["src.controllers"])

app: FastAPI = AppUtils.create_fastapi_app()
app.container = container
set_dispatch_routes(app)

# TODO remove this method in production
# This is only for this boilerplate, don`t use in production environment
# Set up database schema with sync adapter
logging.info("Creating database schema with sync adapter")


async def async_schema_setup():
    """Set up database schema for async adapter."""
    # Use AsyncEngine.begin() for proper transaction handling
    adapter = AsyncSqlAlchemyAdapter()
    async with adapter.session_manager.engine.begin() as conn:
        # Drop all tables (but only if they exist)
        await conn.run_sync(BaseEntity.metadata.drop_all)
        # Create all tables
        await conn.run_sync(BaseEntity.metadata.create_all)


asyncio.gather(async_schema_setup())


if __name__ == "__main__":
    logging.basicConfig(
        level=RuntimeConfig.global_config().ENVIRONMENT.log_level,
        filename="../siteLogs.log",
        format="{'time':'%(asctime)s', 'name': '%(name)s', \
        'level': '%(levelname)s', 'message': '%(message)s'}",
    )

    uvicorn.run(
        app="manage:app",
        access_log=RuntimeConfig.global_config().FASTAPI.ACCESS_LOG,
        backlog=RuntimeConfig.global_config().FASTAPI.BACKLOG,
        date_header=RuntimeConfig.global_config().FASTAPI.DATE_HEADER,
        forwarded_allow_ips=RuntimeConfig.global_config().FASTAPI.FORWARDED_ALLOW_IPS,
        host=RuntimeConfig.global_config().FASTAPI.SERVE_HOST,
        limit_concurrency=RuntimeConfig.global_config().FASTAPI.LIMIT_CONCURRENCY,
        limit_max_requests=RuntimeConfig.global_config().FASTAPI.LIMIT_MAX_REQUESTS,
        port=RuntimeConfig.global_config().FASTAPI.SERVE_PORT,
        proxy_headers=RuntimeConfig.global_config().FASTAPI.PROXY_HEADERS,
        reload=RuntimeConfig.global_config().FASTAPI.RELOAD,
        server_header=RuntimeConfig.global_config().FASTAPI.SERVER_HEADER,
        timeout_graceful_shutdown=RuntimeConfig.global_config().FASTAPI.TIMEOUT_GRACEFUL_SHUTDOWN,
        timeout_keep_alive=RuntimeConfig.global_config().FASTAPI.TIMEOUT_KEEP_ALIVE,
        workers=RuntimeConfig.global_config().FASTAPI.WORKERS_COUNT,
        ws_max_size=RuntimeConfig.global_config().FASTAPI.WS_MAX_SIZE,
        ws_per_message_deflate=RuntimeConfig.global_config().FASTAPI.WS_PER_MESSAGE_DEFLATE,
        ws_ping_interval=RuntimeConfig.global_config().FASTAPI.WS_PING_INTERVAL,
        ws_ping_timeout=RuntimeConfig.global_config().FASTAPI.WS_PING_TIMEOUT,
    )
