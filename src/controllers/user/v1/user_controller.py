from archipy.models.errors import AlreadyExistsError
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.configs.containers import ServiceContainer
from src.logics.user.user_logic import UserLogic
from src.models.dtos.user.domain.v1.user_domain_interface_dtos import CreateUserInputDTOV1, CreateUserOutputDTOV1
from src.models.types.api_router_type import ApiRouterType
from src.utils.utils import Utils

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.USER])


@routerV1.post(
    path="/",
    response_model=CreateUserOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses(
        [
            AlreadyExistsError,
        ],
    ),
)
@inject
async def create_user(
    input_dto: CreateUserInputDTOV1,
    logic: UserLogic = Depends(Provide[ServiceContainer.user_logic]),
) -> CreateUserOutputDTOV1:
    return await logic.create_user(input_dto=input_dto)
