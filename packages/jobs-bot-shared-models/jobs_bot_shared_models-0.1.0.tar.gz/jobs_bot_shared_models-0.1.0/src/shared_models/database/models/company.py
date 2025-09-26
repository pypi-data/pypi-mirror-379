import uuid
import datetime
from typing import Optional
from shared_models.database.utils import Base
from shared_models.enums import SubscriptionType
from sqlalchemy import func, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .vacancy import Vacancy


class CompanyUser(Base):
    __tablename__ = "company_user"

    company_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("company.id"), primary_key=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    added_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    company: Mapped["Company"] = relationship("Company", back_populates="company_users")
    user: Mapped["User"] = relationship("User", back_populates="company_user")

    def __init__(self, user: "User"):
        """
        Initialize a CompanyUser object.

        Args:
            user (User): The associated user.
        """
        self.user = user


class Company(Base):
    __tablename__ = "company"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    reject_message: Mapped[Optional["CompanyRejectMessage"]] = relationship(
        back_populates="company",
        uselist=False,
        cascade="all, delete-orphan",
    )
    accept_message: Mapped[Optional["CompanyAcceptMessage"]] = relationship(
        back_populates="company",
        uselist=False,
        cascade="all, delete-orphan",
    )
    subscription: Mapped[Optional["CompanySubscription"]] = relationship(
        back_populates="company",
        uselist=False,
        cascade="all, delete-orphan",
    )
    company_users: Mapped[list["CompanyUser"]] = relationship(
        back_populates="company", cascade="all, delete-orphan"
    )
    users: AssociationProxy[list["User"]] = association_proxy("company_users", "user")
    vacancies: Mapped[list["Vacancy"]] = relationship(
        back_populates="company", cascade="all, delete-orphan"
    )

    def __init__(self, name: str):
        """
        Initialize a Company object.

        Args:
            name (str): The name of the company.
        """
        self.name = name


class CompanyRejectMessage(Base):
    __tablename__ = "company_reject_message"

    company_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("company.id"), primary_key=True
    )
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    company: Mapped["Company"] = relationship(back_populates="reject_message")

    def __init__(self, message: str, company: Company):
        """
        Initialize a CompanyRejectMessage object.

        Args:
            message (str): The rejection message.
            company (Company): The associated company.
        """
        self.message = message
        self.company = company


class CompanyAcceptMessage(Base):
    __tablename__ = "company_accept_message"

    company_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("company.id"), primary_key=True
    )
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    company: Mapped["Company"] = relationship(back_populates="accept_message")

    def __init__(self, message: str, company: Company):
        """
        Initialize a CompanyAcceptMessage object.

        Args:
            message (str): The acceptance message.
            company (Company): The associated company.
        """
        self.message = message
        self.company = company


class CompanySubscription(Base):
    __tablename__ = "company_subscription"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("company.id"))
    expire_at: Mapped[datetime.datetime] = mapped_column()
    type: Mapped[SubscriptionType] = mapped_column()
    buy_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    company: Mapped["Company"] = relationship(back_populates="subscription")

    def __init__(
        self,
        company: Company,
        expire_at: datetime.datetime,
        type: SubscriptionType,
        buy_at: datetime.datetime | None = None,
    ):
        """
        Initialize a CompanySubscription object.

        Args:
            company (Company): The associated company.
            expire_at (datetime.datetime): The expiration date of the subscription.
            type (SubscriptionType): The type of the subscription.
            buy_at (datetime.datetime | None): The purchase date of the subscription. Defaults to None, which sets it to the current time.
        """
        self.company = company
        self.expire_at = expire_at
        self.type = type
        if buy_at is not None:
            self.buy_at = buy_at
