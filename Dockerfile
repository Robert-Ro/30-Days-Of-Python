FROM python:3.10

WORKDIR /app

VOLUME /source

CMD ["python", "source/main.py"]