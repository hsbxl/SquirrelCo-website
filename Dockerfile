FROM python:3.11-slim-buster

WORKDIR /opt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y libpq-dev build-essential netcat && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "squirrelco.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "600"]