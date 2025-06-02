FROM ubuntu:20.04
COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r ./requirements.txt
COPY . .
CMD python3 ./usd_eur_rate_last_60s_average.py