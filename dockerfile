FROM python:alpine3.11
RUN python --version
#RUN apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install flask 

WORKDIR /app/
COPY . .
 
