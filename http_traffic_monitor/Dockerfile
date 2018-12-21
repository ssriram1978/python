FROM python:3.7-rc-slim
RUN mkdir /http_traffic_monitor
WORKDIR /http_traffic_monitor
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
LABEL author="sriramsridharjob78@gmail.com" \
      version="1.0"
RUN apt-get update
RUN touch /var/log/access.log  # since the program will read this by default
RUN apt-get install -y \
    net-tools \
    vim  \
    wget  \
    w3c-markup-validator  \
    tcpflow  \
    tcpdump
COPY . .
CMD python3 http_traffic_monitor.py