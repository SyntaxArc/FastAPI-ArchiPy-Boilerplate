from archipy.adapters.sqlite.sqlalchemy.adapters import AsyncSQLiteSQLAlchemyAdapter
from dependency_injector import containers, providers

from src.configs.runtime_config import RuntimeConfig
from src.logics.user.user_logic import UserLogic
from src.repositories.user.adapters.user_postgres_adapter import UserPostgresAdapter
from src.repositories.user.user_repository import UserRepository


class ServiceContainer(containers.DeclarativeContainer):
    _config: RuntimeConfig = RuntimeConfig.global_config()
    _postgres_adapter: AsyncSQLiteSQLAlchemyAdapter = providers.ThreadSafeSingleton(AsyncSQLiteSQLAlchemyAdapter)
    _user_postgres_adapter = providers.ThreadSafeSingleton(
        UserPostgresAdapter,
        adapter=_postgres_adapter,
    )
    _user_repository = providers.ThreadSafeSingleton(
        UserRepository,
        postgres_adapter=_user_postgres_adapter,
    )
    user_logic = providers.ThreadSafeSingleton(
        UserLogic,
        repository=_user_repository,
    )
