# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements file into root path in container
COPY requirements.txt .
# Run pip install requirements
RUN pip3 install -r requirements.txt

#Copy contents of /todo_list to a new directory in the container as /app
COPY ./todo_list /app

COPY ./api /app/api

COPY ./base /app/base

# Declare working directory
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

