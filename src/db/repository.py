from sqlalchemy import select

from src.db.database import session_factory
from src.db.models import Email


async def get_email_list():
    async with session_factory() as session:
        result = await session.execute(select(Email))
        email_list_db = result.scalars().all()
        return [email.email for email in email_list_db]
