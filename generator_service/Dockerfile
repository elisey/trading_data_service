FROM python:3.9.5-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY entrypoint.sh .
COPY src .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
