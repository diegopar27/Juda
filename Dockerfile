FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /JUDA

WORKDIR /JUDA

#RUN apt-get update
#RUN apk update \
    #&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    #&& pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y build-essential python3-gdal libpq-dev libmagic-dev git cmake locales gettext

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . /JUDA