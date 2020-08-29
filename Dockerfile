FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt requirements.txt

RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64
RUN  chmod +x /usr/local/bin/dbmate

RUN pip install -r requirements.txt

COPY . .
