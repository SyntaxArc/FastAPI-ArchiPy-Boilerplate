from src.models.dtos.user.repository.user_repository_interface_dtos import (
    CreateUserCommandDTO,
    CreateUserResponseDTO,
)
from src.repositories.user.adapters.user_postgres_adapter import UserPostgresAdapter


class UserRepository:
    def __init__(self, postgres_adapter: UserPostgresAdapter):
        self._postgres_adapter: UserPostgresAdapter = postgres_adapter

    async def create_user(self, input_dto: CreateUserCommandDTO) -> CreateUserResponseDTO:
        return await self._postgres_adapter.create_user(input_dto=input_dto)
