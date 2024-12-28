import asyncio

import httpx

from src.core._redis import redis


async def worker_process_mails():
    while True:
        try:
            emails = await redis.zrange("email_errors", 0, -1, withscores=True)
            print(emails)

            for email, time in emails:
                email: bytes
                url = "https://education.yandex.ru/portal-api/form"
                payload = {
                    "surveyId": "13720008",
                    "data": {
                        "answer_non_profile_email_51926287": email.decode()
                    }
                }
                headers = {
                    "Content-Type": "application/json"
                }

                # Отправка запроса
                async with httpx.AsyncClient() as client:
                    response = await client.post(url, json=payload, headers=headers)

                # Проверка ответа
                if response.status_code == 200:
                    await redis.zrem("email_errors", str(email))
                    continue
                print(f"worker status code: {response.status_code}")
                print(f"worker Headers: {response.headers}")
                print(f"worker Email: {email}")

        except Exception as e:
            print(e)
        await asyncio.sleep(60 * 10)