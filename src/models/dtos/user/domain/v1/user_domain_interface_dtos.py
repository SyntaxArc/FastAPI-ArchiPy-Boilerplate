from datetime import datetime
from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.range_dtos import DateRangeDTO
from archipy.models.dtos.sort_dto import SortDTO
from pydantic import StrictStr

from src.models.types.user_sort_type import UserSortColumnType


class CreateUserInputDTOV1(BaseDTO):
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime


class CreateUserOutputDTOV1(BaseDTO):
    user_uuid: UUID


class GetUserInputDTOV1(BaseDTO):
    user_uuid: UUID


class GetUserOutputDTOV1(BaseDTO):
    user_uuid: UUID
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime | None = None
    activation_status: bool
    created_at: datetime


class UserItemDTOV1(BaseDTO):
    user_uuid: UUID
    first_name: StrictStr
    last_name: StrictStr
    birth_date: datetime | None = None
    activation_status: bool
    created_at: datetime


class SearchUserInputDTOV1(BaseDTO):
    first_name: StrictStr | None = None
    last_name: StrictStr | None = None
    birth_date_range: DateRangeDTO | None = None
    pagination: PaginationDTO
    sort_info: SortDTO[UserSortColumnType]

    @classmethod
    def create(
        cls,
        first_name: str | None = None,
        last_name: str | None = None,
        birth_date_from: datetime | None = None,
        birth_date_to: datetime | None = None,
        page: int = 1,
        page_size: int = 10,
        sort_column: UserSortColumnType = UserSortColumnType.CREATED_AT,
        sort_order: str = "desc",
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[UserSortColumnType](column=sort_column, order=sort_order)
        birth_date_range = None
        if birth_date_from or birth_date_to:
            birth_date_range = DateRangeDTO(from_=birth_date_from, to=birth_date_to)

        return cls(
            first_name=first_name,
            last_name=last_name,
            birth_date_range=birth_date_range,
            pagination=pagination,
            sort_info=sort_info,
        )


class SearchUserOutputDTOV1(BaseDTO):
    users: list[UserItemDTOV1]
    total: int


class UpdateUserRestInputDTOV1(BaseDTO):
    first_name: StrictStr | None = None
    last_name: StrictStr | None = None
    birth_date: datetime | None = None
    activation_status: bool | None = None


class UpdateUserInputDTOV1(UpdateUserRestInputDTOV1):
    user_uuid: UUID


class DeleteUserInputDTOV1(BaseDTO):
    user_uuid: UUID
