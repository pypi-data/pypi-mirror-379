import uuid
import datetime
from shared_models.database.utils import Base
from shared_models.enums import QuestionType, ContentType
from sqlalchemy import func, ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .company import Company
    from .response import VacancyQuestionAnswer, VacancyResponse


class Vacancy(Base):
    __tablename__ = "vacancy"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    company_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("company.id"))
    position: Mapped[str] = mapped_column(Text)
    experience: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    requirements: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    company: Mapped["Company"] = relationship(back_populates="vacancies")
    questions: Mapped[list["VacancyQuestion"]] = relationship(
        back_populates="vacancy", cascade="all, delete-orphan"
    )
    responses: Mapped[list["VacancyResponse"]] = relationship(
        back_populates="vacancy", cascade="all, delete-orphan"
    )

    def __init__(
        self,
        company: "Company",
        position: str,
        experience: str,
        description: str,
        requirements: str,
    ):
        """
        Initialize a Vacancy object.

        Args:
            company (Company): The associated company.
            position (str): The position of the vacancy.
            experience (str): The experience required for the vacancy.
            description (str): The description of the vacancy.
            requirements (str): The requirements of the vacancy.
        """
        self.company = company
        self.position = position
        self.experience = experience
        self.description = description
        self.requirements = requirements


class VacancyQuestion(Base):
    __tablename__ = "vacancy_question"
    __mapper_args__ = {"polymorphic_on": "type", "polymorphic_abstract": True}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    vacancy_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vacancy.id"))
    text: Mapped[str] = mapped_column(Text)
    ordinal_number: Mapped[int] = mapped_column()
    type: Mapped[QuestionType] = mapped_column()

    vacancy: Mapped["Vacancy"] = relationship(back_populates="questions")
    answers: Mapped[list["VacancyQuestionAnswer"]] = relationship(
        back_populates="question", cascade="all, delete-orphan"
    )

    def __init__(self, text: str, ordinal_number: int):
        """
        Initialize an OpenQuestion object.

        Args:
            text (str): The text of the question.
            ordinal_number (int): The ordinal number of the question.
        """
        self.text = text
        self.ordinal_number = ordinal_number


class OpenQuestion(VacancyQuestion):
    __tablename__ = "open_question_info"
    __mapper_args__ = {
        "polymorphic_identity": QuestionType.OPEN,
    }

    id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("vacancy_question.id"), primary_key=True
    )
    response_format: Mapped[ContentType] = mapped_column()

    def __init__(
        self,
        text: str,
        ordinal_number: int,
        response_format: ContentType,
    ):
        """
        Initializes an OpenQuestion object.

        Args:
            text (str): The text of the question.
            ordinal_number (int): The ordinal number of the question.
            response_format (ContentType): The response format of the question.
        """
        super().__init__(text, ordinal_number)
        self.response_format = response_format


class TestQuestion(VacancyQuestion):
    __tablename__ = "test_question_info"
    __mapper_args__ = {
        "polymorphic_identity": QuestionType.TEST,
    }

    id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("vacancy_question.id"), primary_key=True
    )
    continue_if_incorrect: Mapped[bool] = mapped_column()

    options: Mapped[list["TestQuestionOption"]] = relationship(
        back_populates="question"
    )

    def __init__(
        self,
        text: str,
        ordinal_number: int,
        continue_if_incorrect: bool,
    ):
        """
        Initializes a TestQuestion object.

        Args:
            text (str): The text of the question.
            ordinal_number (int): The ordinal number of the question.
            continue_if_incorrect (bool): Whether to continue if the answer is incorrect.
        """
        super().__init__(text, ordinal_number)
        self.continue_if_incorrect = continue_if_incorrect


class TestQuestionOption(Base):
    __tablename__ = "test_question_option"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    question_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test_question_info.id"))
    option: Mapped[str] = mapped_column(String(100))
    is_correct: Mapped[bool] = mapped_column()

    question: Mapped["TestQuestion"] = relationship(back_populates="options")

    def __init__(self, option: str, is_correct: bool):
        """
        Initializes a TestQuestionOption object.

        Args:
            option (str): The option text.
            is_correct (bool): Whether the option is correct.
        """
        self.option = option
        self.is_correct = is_correct
