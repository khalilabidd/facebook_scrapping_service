FROM python:3.9

WORKDIR /fastapi-app

COPY requirements.txt .

pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]