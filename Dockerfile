FROM python:3.14-slim-trixie

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYCODE 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "esports_platform.wsgi", "-b", "0.0.0.0:8000"]
