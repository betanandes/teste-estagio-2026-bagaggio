import sys
from pathlib import Path


if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from database import Base, DATABASE_PATH, SessionLocal, create_database, engine
from entities.user import User


USERS = [
        {"name": "Fernanda Campos", "email": "fernanda.campos@example.com", "password": "K9mP2xQa7L",
         "is_active": True},
        {"name": "Gustavo Ribeiro", "email": "gustavo.ribeiro@example.com", "password": "wR8tY3nLp5",
         "is_active": True},
        {"name": "Helena Batista", "email": "helena.batista@example.com", "password": "Qz4Mx8Vb1K", "is_active": False},
        {"name": "Igor Carvalho", "email": "igor.carvalho@example.com", "password": "N7cDf2Pq9W", "is_active": True},
        {"name": "Juliana Moraes", "email": "juliana.moraes@example.com", "password": "mL5rTy8Zx2", "is_active": True},
        {"name": "Kleber Azevedo", "email": "kleber.azevedo@example.com", "password": "P1vBn6Qw3E", "is_active": True},
        {"name": "Larissa Cunha", "email": "larissa.cunha@example.com", "password": "X8sDf4Gh7J", "is_active": False},
        {"name": "Marcelo Porto", "email": "marcelo.porto@example.com", "password": "aZ9kLm2Np6", "is_active": True},
        {"name": "Natalia Freire", "email": "natalia.freire@example.com", "password": "R4tYu8Io1P", "is_active": True},
        {"name": "Otavio Falcao", "email": "otavio.falcao@example.com", "password": "jK3hGf7Ds9", "is_active": True},
        {"name": "Patricia Neves", "email": "patricia.neves@example.com", "password": "V2bNm8Cx5Z", "is_active": True},
        {"name": "Renato Tavares", "email": "renato.tavares@example.com", "password": "uY6iOp3Lk8", "is_active": False},
        {"name": "Simone Duarte", "email": "simone.duarte@example.com", "password": "M1qWe9Rt4Y", "is_active": True},
        {"name": "Talita Braga", "email": "talita.braga@example.com", "password": "cV7bNm2As5", "is_active": True},
        {"name": "Ulisses Prado", "email": "ulisses.prado@example.com", "password": "F8gHj3Kl6P", "is_active": True},
        {"name": "Vanessa Reis", "email": "vanessa.reis@example.com", "password": "zX4cV9Bn1M", "is_active": False},
        {"name": "Wagner Pires", "email": "wagner.pires@example.com", "password": "T6yUi2Op8Q", "is_active": True},
        {"name": "Yuri Matos", "email": "yuri.matos@example.com", "password": "nB5vCx7Za3", "is_active": True},
        {"name": "Zilda Rocha", "email": "zilda.rocha@example.com", "password": "L9kJh4Gf2D", "is_active": True},
        {"name": "Aline Gomes", "email": "aline.gomes@example.com", "password": "pQ8wEr3Ty6", "is_active": True},
        {"name": "Brenda Lopes", "email": "brenda.lopes@example.com", "password": "X1zCv7Bn4M", "is_active": False},
        {"name": "Cesar Martins", "email": "cesar.martins@example.com", "password": "rT5yUi9Op2", "is_active": True},
        {"name": "Debora Silva", "email": "debora.silva@example.com", "password": "J6hGf3Ds8A", "is_active": True},
        {"name": "Erick Nascimento", "email": "erick.nascimento@example.com", "password": "wQ2eRt7Yu5",
         "is_active": True},
        {"name": "Fabiana Costa", "email": "fabiana.costa@example.com", "password": "M4nBc8Vx1Z", "is_active": False},
        {"name": "Gilberto Dias", "email": "gilberto.dias@example.com", "password": "aS9dFg2Hj6", "is_active": True},
        {"name": "Hugo Barros", "email": "hugo.barros@example.com", "password": "K3lPq7We4R", "is_active": True},
        {"name": "Isabela Melo", "email": "isabela.melo@example.com", "password": "uJ8kLm1Np5", "is_active": True},
        {"name": "Jonas Vieira", "email": "jonas.vieira@example.com", "password": "C6vBn2Mx9Q", "is_active": False},
        {"name": "Karina Rocha", "email": "karina.rocha@example.com", "password": "T4gHj8Kl3P", "is_active": True},
        {"name": "Leonardo Souza", "email": "leonardo.souza@example.com", "password": "yU1iOp7As5", "is_active": True},
        {"name": "Monica Ferreira", "email": "monica.ferreira@example.com", "password": "V9bNm3Cx6Z",
         "is_active": True},
        {"name": "Nicolas Andrade", "email": "nicolas.andrade@example.com", "password": "qW2eRt8Yu4",
         "is_active": False},
        {"name": "Priscila Castro", "email": "priscila.castro@example.com", "password": "H5jKl1Mn7B",
         "is_active": True},
        {"name": "Ricardo Alves", "email": "ricardo.alves@example.com", "password": "xC8vBn4Mz2", "is_active": True},
        {"name": "Suelen Nogueira", "email": "suelen.nogueira@example.com", "password": "D3fGh9Jk6L",
         "is_active": True},
        {"name": "Tiago Ramos", "email": "tiago.ramos@example.com", "password": "pO7iUy2Tr5", "is_active": False},
        {"name": "Viviane Moura", "email": "viviane.moura@example.com", "password": "Z1xCv8Bn4M", "is_active": True},
        {"name": "William Santana", "email": "william.santana@example.com", "password": "N6mQw3Er9T",
         "is_active": True},
        {"name": "Yasmin Freitas", "email": "yasmin.freitas@example.com", "password": "G4hJk7Lp2V", "is_active": True},
    ]


def run_seed() -> None:
    create_database()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    for item in USERS:
        db.add(User(**item))
    db.commit()
    db.close()


if __name__ == "__main__":
    run_seed()
    print(f"SQLite criado com {len(USERS)} usuarios em: {DATABASE_PATH}")
