FROM python:3.8-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3
RUN pip install pika

ENV PYTHONUNBUFFERED 1

COPY ./seach.py ./seach.py

CMD ["python", "seach.py"]