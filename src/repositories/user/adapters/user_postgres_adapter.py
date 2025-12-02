from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.base.sqlalchemy.ports import AsyncSQLAlchemyPort
from archipy.adapters.sqlite.sqlalchemy.adapters import AsyncSQLiteSQLAlchemyAdapter
from archipy.models.errors import NotFoundError
from archipy.models.types.base_types import FilterOperationType
from sqlalchemy import delete, select, update
from sqlalchemy.sql.expression import Select, Update

from src.models.dtos.user.repository.user_repository_interface_dtos import (
    CreateUserCommandDTO,
    CreateUserResponseDTO,
    DeleteUserCommandDTO,
    GetUserQueryDTO,
    GetUserResponseDTO,
    SearchUserQueryDTO,
    SearchUserResponseDTO,
    UpdateUserCommandDTO,
)
from src.models.entities.user_entity import UserEntity


class UserPostgresAdapter(SQLAlchemyFilterMixin):
    def __init__(self, adapter: AsyncSQLiteSQLAlchemyAdapter) -> None:
        self._adapter: AsyncSQLAlchemyPort = adapter

    async def create_user(self, input_dto: CreateUserCommandDTO) -> CreateUserResponseDTO:
        user: UserEntity = UserEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=user)
        return CreateUserResponseDTO.model_validate(obj=result)

    async def get_user(self, input_dto: GetUserQueryDTO) -> GetUserResponseDTO:
        select_query = select(UserEntity).where(UserEntity.user_uuid == input_dto.user_uuid)

        result = await self._adapter.execute(statement=select_query)
        user = result.scalar()

        if not user:
            raise NotFoundError(resource_type=UserEntity.__name__)

        return GetUserResponseDTO.model_validate(obj=user)

    async def search_users(self, input_dto: SearchUserQueryDTO) -> SearchUserResponseDTO:
        query: Select = select(UserEntity)

        if input_dto.first_name:
            query = self._apply_filter(
                query=query,
                field=UserEntity.first_name,
                value=f"%{input_dto.first_name}%",
                operation=FilterOperationType.ILIKE,
            )

        if input_dto.last_name:
            query = self._apply_filter(
                query=query,
                field=UserEntity.last_name,
                value=f"%{input_dto.last_name}%",
                operation=FilterOperationType.ILIKE,
            )

        if input_dto.birth_date_range:
            if input_dto.birth_date_range.from_:
                query = self._apply_filter(
                    query=query,
                    field=UserEntity.birth_date,
                    value=input_dto.birth_date_range.from_,
                    operation=FilterOperationType.GREATER_THAN_OR_EQUAL,
                )
            if input_dto.birth_date_range.to:
                query = self._apply_filter(
                    query=query,
                    field=UserEntity.birth_date,
                    value=input_dto.birth_date_range.to,
                    operation=FilterOperationType.LESS_THAN_OR_EQUAL,
                )

        users, total = await self._adapter.execute_search_query(
            query=query,
            entity=UserEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchUserResponseDTO(users=users, total=total)

    async def update_user(self, input_dto: UpdateUserCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"user_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(UserEntity).where(UserEntity.user_uuid == input_dto.user_uuid).values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=UserEntity.__name__)

    async def delete_user(self, input_dto: DeleteUserCommandDTO) -> None:
        delete_query = delete(UserEntity).where(UserEntity.user_uuid == input_dto.user_uuid)

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=UserEntity.__name__)
