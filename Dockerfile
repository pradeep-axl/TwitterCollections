FROM python:3.7.6-buster
MAINTAINER Pradeep Kumar

RUN mkdir /TwitterCollection
WORKDIR /TwitterCollection

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "-u", "twitter_collection.py"]
