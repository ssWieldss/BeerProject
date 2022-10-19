FROM python:3.9
ENV PYTHONUNBUFFERED = 1
WORKDIR beerproject
COPY beerproject/beerproject/requirements.txt /beerproject/
RUN pip install -r requirements.txt
COPY /beerproject /beerproject/