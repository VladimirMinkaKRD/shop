FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN mkdir "code"

COPY . /code
COPY req.txt /code
WORKDIR /code

RUN pip3 install --upgrade pip
RUN pip3 install -r req.txt


