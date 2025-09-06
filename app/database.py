import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Convert PostgreSQL URL to async version
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True for development
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
print('connection established !!', async_session)