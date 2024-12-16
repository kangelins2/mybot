import pandas as pd
from aiogram import Router
from aiogram.types import FSInputFile, Message

from aiogram.filters import Command
from sqlalchemy import select

from src.core.credentails import ALLOWED_USER_IDS
from src.db.database import session_factory
from src.db.models import Email

router = Router()


@router.message(Command('download_emails'))
async def download_price(message: Message):
    async with (session_factory() as db):
        if message.from_user.id not in ALLOWED_USER_IDS:
            await message.answer("")
            return
        email_list_db = await db.execute(select(Email))
        email_list = []
        for email in email_list_db.scalars().fetchall():
            email_list.append(email.email)
    df = pd.DataFrame(email_list, columns=['Emails'])
    csv_file = 'emails.csv'
    df.to_csv(csv_file, index=False)
    document = FSInputFile('emails.csv')
    await message.answer_document(document)