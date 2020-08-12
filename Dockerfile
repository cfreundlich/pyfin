FROM python:3.8
RUN mkdir /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt
COPY . /code
WORKDIR /code