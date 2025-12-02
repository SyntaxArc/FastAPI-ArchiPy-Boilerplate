from archipy.helpers.utils.base_utils import BaseUtils
from archipy.models.errors import UnauthenticatedError, UnknownError, UnavailableError, InvalidArgumentError

from fastapi import FastAPI

from src.controllers.user.v1 import user_controller


def set_dispatch_routes(app: FastAPI) -> None:
    common_private_response = BaseUtils.get_fastapi_exception_responses(
        [UnauthenticatedError, UnknownError, UnavailableError, InvalidArgumentError],
    )
    app.include_router(router=user_controller.routerV1, prefix="/api/v1/users", responses=common_private_response)
