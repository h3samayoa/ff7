FROM python:3.11-slim-bullseye

WORKDIR /app

VOLUME /app/configs

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "webscrape.py"]

