from fastapi import APIRouter

from src.endpoints.models import EmailRequest
from src.db.database import session_factory
from src.db.models import Email

router = APIRouter()

@router.post("/emails/")
async def save_email(email: EmailRequest):
    async with session_factory() as db:
        email_db = Email(email=email.email)
        db.add(email_db)
        await db.commit()
    return {"status": "Ok"}
