FROM python:alpine

WORKDIR /app

RUN pip install pymongo

COPY . /app

CMD [ "python", "main.py" ]