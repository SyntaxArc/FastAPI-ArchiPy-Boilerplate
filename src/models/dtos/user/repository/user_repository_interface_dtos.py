from datetime import datetime
from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.range_dtos import DateRangeDTO
from archipy.models.dtos.sort_dto import SortDTO
from pydantic import StrictStr

from src.models.types.user_sort_type import UserSortColumnType


class CreateUserCommandDTO(BaseDTO):
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime


class CreateUserResponseDTO(BaseDTO):
    user_uuid: UUID
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime | None = None


class GetUserQueryDTO(BaseDTO):
    user_uuid: UUID


class GetUserResponseDTO(BaseDTO):
    user_uuid: UUID
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime | None = None
    activation_status: bool
    created_at: datetime


class UserItemDTO(BaseDTO):
    user_uuid: UUID
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime | None = None
    activation_status: bool
    created_at: datetime


class SearchUserQueryDTO(BaseDTO):
    first_name: StrictStr | None = None
    last_name: StrictStr | None = None
    birth_date_range: DateRangeDTO | None = None
    pagination: PaginationDTO
    sort_info: SortDTO[UserSortColumnType]


class SearchUserResponseDTO(BaseDTO):
    users: list[UserItemDTO]
    total: int


class UpdateUserCommandDTO(BaseDTO):
    user_uuid: UUID
    first_name: StrictStr | None = None
    last_name: StrictStr | None = None
    birth_date: datetime | None = None
    activation_status: bool | None = None


class DeleteUserCommandDTO(BaseDTO):
    user_uuid: UUID
