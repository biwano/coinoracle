FROM python:3.9.21

RUN mkdir /data
COPY . /src
WORKDIR /src
RUN pip3 install -r requirements.txt

CMD [ "python", "./main.py" ]