from archipy.adapters.orm.sqlalchemy.adapters import (
    AsyncSqlAlchemyAdapter,
    SqlAlchemyFilterMixin,
)
from archipy.adapters.orm.sqlalchemy.ports import AsyncSqlAlchemyPort

from src.models.dtos.user.repository.user_repository_interface_dtos import (
    CreateUserCommandDTO,
    CreateUserResponseDTO,
)
from src.models.entities.user_entity import UserEntity


class UserPostgresAdapter(SqlAlchemyFilterMixin):
    def __init__(self, adapter: AsyncSqlAlchemyAdapter) -> None:
        self._adapter: AsyncSqlAlchemyPort = adapter

    async def create_user(self, input_dto: CreateUserCommandDTO) -> CreateUserResponseDTO:
        user: UserEntity = UserEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=user)
        return CreateUserResponseDTO.model_validate(obj=result)
