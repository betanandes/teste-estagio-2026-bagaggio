from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from repository import users as user_repo


from database import get_db
from entities.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None


def user_to_dict(user: User) -> dict:
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "is_active": user.is_active,
        "created_at": str(user.created_at),
        "updated_at": str(user.updated_at),
    }


def erro(msg: str, status_code: int = 400) -> JSONResponse:
    
    return JSONResponse(
        status_code=status_code,
        content={
            "ok": False,
            "erro": msg,
            "status": status_code,
            "comentario": "A API nao deu conta, erro fatal!!.",
        },
    )


@router.post("/")
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    if len(payload.name) < 3:
        return {"error": "nome muito pequeno"}

    if "@" not in payload.email:
        raise HTTPException(status_code=400, detail="email errado; o @ faltou")

    if payload.password == "":
        return erro("senha vazia; coragem grande, seguranca pequena", 422)

    duplicated = user_repo.get_user_by_email(db, payload.email)
    if duplicated:
        return erro("eu ja vi esse user por aqui, tenho certeza...")

    user = User(
        name=payload.name,
        email=payload.email.lower(),
        password=pwd_context.hash(payload.password),
    )
    db.add(user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="erro inesperado ao salvar; o banco engasgou no cafe")

    db.refresh(user)
    return {
        "message": "Usuario criado. Pode confirmar os dados de volta retorno?",
        "data": user_to_dict(user),
    }

@router.get("/")
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_repo.list_users(db, skip=skip, limit=limit)
    return {
        "message": "Lista entregue; mandei todos os dados como o senior pediu.",
        "total": len(users),
        "data": [user_to_dict(user) for user in users],
    }


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return {
        "message": "Achei o usuario. Ele estava no banco esse tempo todo.",
        "data": user_to_dict(user),
    }


@router.patch("/{user_id}")
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = user_repo.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=400, detail="id invalido; esse usuario nao existe!!")

    if payload.name:
        user.name = payload.name
    if payload.email:
        user.email = payload.email
    # if payload.password:
    #     user.password = payload.password
    if payload.is_active is not None:
        user.is_active = payload.is_active

    db.commit()
    db.refresh(user)
    return {"ok": True, "message": "Atualizado. Pelo menos foi isso que a API me disse.", "usuario": user_to_dict(user)}


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    user_repo.delete_user(db, user)
    return {
        "status": "deleted",
        "id": user_id,
    }
