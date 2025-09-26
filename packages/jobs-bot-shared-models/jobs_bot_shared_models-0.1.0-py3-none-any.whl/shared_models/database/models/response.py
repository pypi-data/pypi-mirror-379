import uuid
import datetime
from shared_models.database.utils import Base
from shared_models.enums import QuestionType, ContentType
from sqlalchemy import func, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vacancy import Vacancy, VacancyQuestion, TestQuestionOption
    from .user import User


class VacancyResponse(Base):
    __tablename__ = "vacancy_response"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    vacancy_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vacancy.id"))
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    vacancy: Mapped["Vacancy"] = relationship(back_populates="responses")
    user: Mapped["User"] = relationship(back_populates="responses")
    answers: Mapped[list["VacancyQuestionAnswer"]] = relationship(
        back_populates="response", cascade="all, delete-orphan"
    )

    def __init__(
        self,
        vacancy: "Vacancy",
        user: "User",
    ):
        """
        Initializes a VacancyResponse object.

        Args:
            vacancy (Vacancy): The associated vacancy.
            user (User): The associated user.
        """
        self.vacancy = vacancy
        self.user = user


class VacancyQuestionAnswer(Base):
    __tablename__ = "vacancy_question_answer"
    __mapper_args__ = {"polymorphic_on": "type", "polymorphic_abstract": True}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    response_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vacancy_response.id"))
    question_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vacancy_question.id"))
    type: Mapped[QuestionType] = mapped_column()

    response: Mapped["VacancyResponse"] = relationship(back_populates="answers")
    question: Mapped["VacancyQuestion"] = relationship(back_populates="answers")

    def __init__(
        self,
        question: "VacancyQuestion",
    ):
        """
        Initializes the object with a given VacancyQuestion.

        Args:
            question (VacancyQuestion): The question associated with this response.
        """
        self.question = question


class OpenQuestionAnswer(VacancyQuestionAnswer):
    __tablename__ = "open_question_answer_info"
    __mapper_args__ = {
        "polymorphic_identity": QuestionType.OPEN,
    }

    id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("vacancy_question_answer.id"), primary_key=True
    )
    content_type: Mapped[ContentType] = mapped_column()
    text: Mapped[str | None] = mapped_column(Text)
    content_file_id: Mapped[uuid.UUID | None] = mapped_column()

    @validates("content_type")
    def validate_content_type(self, _, content_type):
        if content_type == ContentType.ANY:
            raise ValueError("Content type cannot be ANY for OpenQuestionAnswerInfo")
        return content_type

    @validates("content_file_id", "text")
    def validate_content(self, key, value):
        if (
            key == "content_file_id"
            and self.content_type == ContentType.TEXT
            and value is not None
        ):
            raise ValueError("content_file_id must be None if content_type is TEXT")
        if (
            key == "text"
            and self.content_type != ContentType.TEXT
            and value is not None
        ):
            raise ValueError("text must be None if content_type is not TEXT")
        return value

    def __init__(
        self,
        question: "VacancyQuestion",
        content_type: ContentType,
        text: str | None = None,
        content_file_id: uuid.UUID | None = None,
    ):
        """
        Initializes an OpenQuestionAnswer object.

        Args:
            question (VacancyQuestion): The question associated with this answer.
            content_type (ContentType): The type of content of the answer.
            text (str | None): The text content of the answer. Defaults to None.
            content_file_id (uuid.UUID | None): The id of the content file of the answer. Defaults to None.
        """
        super().__init__(question)
        self.content_type = content_type
        self.text = text
        self.content_file_id = content_file_id


class TestQuestionAnswer(VacancyQuestionAnswer):
    __tablename__ = "test_question_answer_info"
    __mapper_args__ = {
        "polymorphic_identity": QuestionType.TEST,
    }

    id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("vacancy_question_answer.id"), primary_key=True
    )
    option_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test_question_option.id"))

    option: Mapped["TestQuestionOption"] = relationship()

    def __init__(
        self,
        question: "VacancyQuestion",
        option: "TestQuestionOption",
    ):
        """
        Initializes a TestQuestionAnswer object.

        Args:
            question (VacancyQuestion): The question associated with this answer.
            option (TestQuestionOption): The option associated with this answer.
        """
        super().__init__(question)
        self.option = option
