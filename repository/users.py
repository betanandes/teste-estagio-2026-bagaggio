from sqlalchemy import select
from sqlalchemy.orm import Session

from entities.user import User, utc_now


def list_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    statement = select(User).offset(skip).limit(limit)
    return list(db.scalars(statement).all())


def get_user(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return db.scalar(statement)


def create_user(db: Session, name: str, email: str, password: str) -> User:
    user = User(
        name=name.strip(),
        email=email.strip().lower(),
        password=password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(
    db: Session,
    user: User,
    *,
    name: str | None = None,
    email: str | None = None,
    password: str | None = None,
    is_active: bool | None = None,
) -> User:
    if name:
        user.name = name.strip()
    if email:
        user.email = email
    if password:
        user.password = password
    if is_active:
        user.is_active = is_active

    user.updated_at = utc_now()
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()
