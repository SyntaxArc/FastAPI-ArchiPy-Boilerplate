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
from src.repositories.user.adapters.user_postgres_adapter import UserPostgresAdapter


class UserRepository:
    def __init__(self, postgres_adapter: UserPostgresAdapter):
        self._postgres_adapter: UserPostgresAdapter = postgres_adapter

    async def create_user(self, input_dto: CreateUserCommandDTO) -> CreateUserResponseDTO:
        return await self._postgres_adapter.create_user(input_dto=input_dto)

    async def get_user(self, input_dto: GetUserQueryDTO) -> GetUserResponseDTO:
        return await self._postgres_adapter.get_user(input_dto=input_dto)

    async def search_users(self, input_dto: SearchUserQueryDTO) -> SearchUserResponseDTO:
        return await self._postgres_adapter.search_users(input_dto=input_dto)

    async def update_user(self, input_dto: UpdateUserCommandDTO) -> None:
        await self._postgres_adapter.update_user(input_dto=input_dto)

    async def delete_user(self, input_dto: DeleteUserCommandDTO) -> None:
        await self._postgres_adapter.delete_user(input_dto=input_dto)
