from contextlib import contextmanager
from datetime import UTC, datetime

from sqlalchemy import Boolean, DateTime, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from essay_bot.config import settings


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_user_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    chat_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    username: Mapped[str | None] = mapped_column(String(255), nullable=True)
    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )


connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, future=True, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope() -> Session:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def upsert_user(
    telegram_user_id: int,
    chat_id: int,
    username: str | None,
    first_name: str | None,
) -> User:
    with session_scope() as session:
        existing = session.scalar(select(User).where(User.telegram_user_id == telegram_user_id))
        if existing:
            existing.chat_id = chat_id
            existing.username = username
            existing.first_name = first_name
            existing.is_active = True
            session.add(existing)
            session.flush()
            session.refresh(existing)
            return existing

        user = User(
            telegram_user_id=telegram_user_id,
            chat_id=chat_id,
            username=username,
            first_name=first_name,
            is_active=True,
        )
        session.add(user)
        session.flush()
        session.refresh(user)
        return user


def list_active_users() -> list[User]:
    with session_scope() as session:
        users = session.scalars(select(User).where(User.is_active.is_(True))).all()
        return list(users)
