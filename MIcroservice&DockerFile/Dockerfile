#FROM python:3.9
FROM ubuntu:20.04
COPY requirements.txt ./assignment2/requirements.txt

RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r ./assignment2/requirements.txt
COPY . .
CMD python3 /assignement2/usd_eur_rate_last_60s_average.py