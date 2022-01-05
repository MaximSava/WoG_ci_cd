FROM python:3.8-slim

RUN mkdir /wog
ADD . /wog
RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get -y install gcc
RUN apt-get -y install nano
RUN apt-get -y install net-tools
RUN apt-get -y install curl
RUN pip install -r /wog/requirements.txt
EXPOSE 5000
WORKDIR /wog
ENTRYPOINT ["python"]
CMD ["MainScores.py"]
