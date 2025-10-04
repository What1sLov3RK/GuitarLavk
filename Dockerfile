FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=GuitarLavk.settings \
    PYTHONUNBUFFERED=1

CMD gunicorn GuitarLavk.wsgi:application --bind 0.0.0.0:${PORT:-8000}
