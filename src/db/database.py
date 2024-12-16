import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.core.credentails import settings


def db_setup():
    db_engine = create_async_engine(settings.DATABASE_URL.unicode_string())
    db_session_factory = async_sessionmaker(db_engine)
    return db_engine, db_session_factory


session_factory: async_sessionmaker[AsyncSession]
engine, session_factory = db_setup()
