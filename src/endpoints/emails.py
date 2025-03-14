import time

import httpx
from fastapi import APIRouter

from src.core._redis import redis
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
            "answer_non_profile_email_51926287": str(email.email)
        }
    }
    headers = {
        "Content-Type": "application/json"
    }

    # Отправка запроса
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

    # Проверка ответа
    if response.status_code != 200:
        await redis.zadd("email_errors", {str(email.email): time.time()})
        print(f"Headers: {response.headers}")
        print(f"Email: {email.email}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

    return {"status": "Ok"}
