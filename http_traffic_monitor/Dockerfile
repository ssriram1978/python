FROM python:3.7-rc-slim
RUN mkdir /http_traffic_monitor
WORKDIR /http_traffic_monitor
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
    tcpdump \
    python3-pip
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip install requests
RUN pip install request
#RUN pip install http
COPY . .
CMD python3 http_log_analyzer/http_log_analyzer.py
