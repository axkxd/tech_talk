FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /tech_talk
COPY ./tech_talk /tech_talk/
WORKDIR /tech_talk

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
