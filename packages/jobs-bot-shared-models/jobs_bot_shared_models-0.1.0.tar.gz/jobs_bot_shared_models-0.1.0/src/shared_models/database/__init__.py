from .utils import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB


if POSTGRES_USER == "" or POSTGRES_PASSWORD == "" or POSTGRES_DB == "":
    raise RuntimeError("Postgres env vars not set")


from .utils import async_session, engine, DATABASE_URL

__all__ = ["async_session", "engine", "DATABASE_URL"]
