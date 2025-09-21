from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mYsecurEpassworD@localhost/alembic_db2"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mYsecurEpassworD@host.docker.internal:5432/alembic_db2"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
