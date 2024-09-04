FROM ubuntu:20.04
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ADD wiz_server /app/wiz_server
ADD migrations /app/migrations

RUN apt-get update && apt-get -y install curl
RUN apt-get install -y python3-pip
RUN apt install -y python3-testresources
RUN pip3 install --upgrade pip

ADD wiz_server/requirements.txt /app
RUN pip3 install -r /app/requirements.txt

RUN ls
RUN locale -a

# RUN locale-gen en_US en_US.UTF-8
# RUN dpkg-reconfigure locales

# RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

COPY wiz_server/wsgi.py /app
COPY wiz_server/entrypoint.sh /app

RUN chmod +x ./entrypoint.sh
