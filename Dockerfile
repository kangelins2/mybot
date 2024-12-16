FROM python:3.12-slim

WORKDIR /usr/app

COPY requerements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]