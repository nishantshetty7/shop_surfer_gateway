FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add gcc python3-dev musl-dev
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt