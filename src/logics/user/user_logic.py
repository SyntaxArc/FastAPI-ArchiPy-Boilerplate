from archipy.helpers.decorators.sqlalchemy_atomic import async_sqlalchemy_atomic_decorator
from dependency_injector.wiring import inject

from src.models.dtos.user.domain.v1.user_domain_interface_dtos import (
    CreateUserInputDTOV1,
    CreateUserOutputDTOV1,
)
from src.models.dtos.user.repository.user_repository_interface_dtos import (
    CreateUserCommandDTO,
    CreateUserResponseDTO,
)
from src.repositories.user.user_repository import UserRepository


class UserLogic:
    @inject
    def __init__(self, repository: UserRepository) -> None:
        self._repository: UserRepository = repository

    @async_sqlalchemy_atomic_decorator
    async def create_user(self, input_dto: CreateUserInputDTOV1) -> CreateUserOutputDTOV1:
        command: CreateUserCommandDTO = CreateUserCommandDTO.model_validate(obj=input_dto)
        response: CreateUserResponseDTO = await self._repository.create_user(input_dto=command)
        return CreateUserOutputDTOV1.model_validate(obj=response)
