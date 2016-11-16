FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
CMD gunicorn -b 0.0.0.0:8000 -R item_master:app
EXPOSE 8000
