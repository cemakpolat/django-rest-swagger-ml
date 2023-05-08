FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update && apt-get install -y gcc
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
COPY . /app/
#CMD ["python3", "manage.py","runserver"]
