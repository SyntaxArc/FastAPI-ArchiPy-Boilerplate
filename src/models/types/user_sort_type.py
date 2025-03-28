from enum import Enum


class UserSortColumnType(str, Enum):
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    BIRTH_DATE = "birth_date"
    CREATED_AT = "created_at"
