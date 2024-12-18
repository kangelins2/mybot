import httpx
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

    url = "https://education.yandex.ru/portal-api/form"
    payload = {
        "surveyId": "13720008",
        "data": {
            "answer_non_profile_email_51926287": email.email
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    # Отправка запроса
    response = httpx.post(url, json=payload, headers=headers)

    # Проверка ответа
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

    return {"status": "Ok"}