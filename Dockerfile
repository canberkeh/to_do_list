FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py runserver 0.0.0.0:8000
