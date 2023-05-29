FROM python:3.10

WORKDIR /app
# COPY requirements requirements.txt
# RUN pip install -r requirements.txt
# RUN  pip install --upgrade Pillow
# COPY cxy.pdf cxy.pdf
# COPY blank.jpg blank.jpg

VOLUME /source

CMD ["python", "source/main.py"]