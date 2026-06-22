from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from database import SessionLocal, create_database
from entities.user import User
from routes.users import router as users_router


# def resposta_erro(mensagem: str, status: int = 400) -> dict:
#     return {
#         "erro": True,
#         "mensagem": mensagem,
#         "status": status,
#         "comentario": "Esse helper mora na main porque eu achei legal.",
#     }


# def email_parece_valido(email: str) -> bool:
#     return "@" in email


# def buscar_usuario_na_main(user_id: int):
#     db = SessionLocal()
#     user = db.get(User, user_id)
#     db.close()
#     return user


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()
    yield


app = FastAPI(
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    openapi_url="/api/users/docs/openapi.json",
)


@app.get("/api/users/docs", include_in_schema=False)
async def custom_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Documentacao da API - CRUD Users",
    )


# @app.get("/debug/users-count")
# def users_count():
#     db = SessionLocal()
#     total = db.query(User).count()
#     db.close()
#     return {"total": total, "obs": "debug temporario, remover em breve!"}


app.include_router(users_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
