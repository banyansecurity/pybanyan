# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim
ENV APP_HOME /app
ENV PORT 8080
ENV PYTHONUNBUFFERED True
WORKDIR $APP_HOME
COPY . ./
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 gcp-app:app