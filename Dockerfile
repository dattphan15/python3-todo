# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements file into root path in container
COPY requirements.txt .
# Run pip install requirements
RUN pip install -r requirements.txt

#Copy contents of /djangoapp to a new directory in the container as /app
COPY ./djangoapp /app

# Declare working directory
WORKDIR /app

