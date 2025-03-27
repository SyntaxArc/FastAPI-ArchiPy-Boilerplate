import uuid
from datetime import datetime

from archipy.models.entities.sqlalchemy.base_entities import (
    UpdatableDeletableEntity,
)
from sqlalchemy import UUID, VARCHAR, Column, Date, DateTime
from sqlalchemy.orm import Mapped, Synonym, mapped_column

from src.utils.utils import Utils


class UserEntity(UpdatableDeletableEntity):
    __tablename__ = "users"
    user_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("user_uuid")
    first_name: Mapped[str] = mapped_column(type_=VARCHAR(255), nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, index=True)
    birth_date: Mapped[Date] = mapped_column(Date, nullable=True, index=True)
    activation_status: Mapped[str] = mapped_column(default=True, index=True)
    hashed_password: Mapped[str] = mapped_column(VARCHAR(320), nullable=True)
    # don`t use this format in production
    created_at: Mapped[datetime] = Column(DateTime(), default=Utils.get_datetime_utc_now, nullable=False)
