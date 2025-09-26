import uuid
import datetime
from typing import Optional
from shared_models.database.utils import Base
from sqlalchemy import func, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .company import Company, CompanyUser
    from .response import VacancyResponse


class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    telegram_account: Mapped[Optional["TelegramUser"]] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )
    company_user: Mapped[Optional["CompanyUser"]] = relationship(
        back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    company: AssociationProxy[Optional["Company"]] = association_proxy(
        "company_user", "company"
    )
    responses: Mapped[list["VacancyResponse"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __init__(self, name: str | None = None):
        """
        Initialize a User object.

        Args:
            name (str | None): The name of the user. Defaults to None.
        """
        self.name = name


class TelegramUser(Base):
    __tablename__ = "telegram_user"

    telegram_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    username: Mapped[str | None] = mapped_column(String(40))

    user: Mapped[User] = relationship(back_populates="telegram_account")

    def __init__(self, telegram_id: int, user: User, username: str | None = None):
        """
        Initialize a TelegramUser object.

        Args:
            telegram_id (int): The telegram id of the user.
            user (User): The user object associated with the telegram user.
            username (str | None): The username of the telegram user. Defaults to None.
        """
        self.telegram_id = telegram_id
        self.username = username
        self.user = user
