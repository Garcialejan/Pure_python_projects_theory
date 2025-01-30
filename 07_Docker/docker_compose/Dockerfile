FROM python:3.12.8-alpine3.21
WORKDIR /code
ENV FASTAPI_APP=app.py
ENV FASTAPI_RUN_HOST = 0.0.0.0
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["fastapi", "run"]