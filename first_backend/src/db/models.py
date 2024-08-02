from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from db.connection import async_engine

Base = declarative_base()


class Domain(Base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True)
    domain = Column(String)
    public_domain = Column(String)


async def init_models():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
