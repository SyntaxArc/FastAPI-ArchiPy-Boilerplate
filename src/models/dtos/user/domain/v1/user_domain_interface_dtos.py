from datetime import datetime
from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr


class CreateUserInputDTOV1(BaseDTO):
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime


class CreateUserOutputDTOV1(BaseDTO):
    user_uuid: UUID
