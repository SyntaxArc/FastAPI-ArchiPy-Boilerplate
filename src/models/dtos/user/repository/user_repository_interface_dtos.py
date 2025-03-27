from datetime import datetime
from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr


class CreateUserCommandDTO(BaseDTO):
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime


class CreateUserResponseDTO(BaseDTO):
    user_uuid: UUID
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime | None = None
