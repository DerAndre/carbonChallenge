FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

LABEL Name=mula-backend Version=1.0.0
EXPOSE 8000

RUN apt-get update && apt install python-dev -y

WORKDIR /app

RUN ls -la

COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
COPY ./carbonChallenge /app/

RUN python3 -m pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN ["python", "manage.py", "migrate"]
RUN ["python", "manage.py", "init_usage_types"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
