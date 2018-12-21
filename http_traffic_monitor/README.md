
How to instructions:
--------------------
tar -xzvf http_traffic_monitor.tar.gz

cd http_traffic_monitor

docker build . -t ssriram1978/http_traffic_monitor:latest

docker run -itd ssriram1978/http_traffic_monitor:latest

(or)

docker swarm init

docker stack deploy -c docker-compose.yml http_traffic_monitor

(or)

docker-compose up -f docker-compose-no-swarm.yml -d 

Explanation:
-------------
This is a Python package.

The package name is http_traffic_monitor.

It has 3 sub components.. 

HTTP Log Analyzer.
-----------------
The main entry point is http_log_analyzer/http_log_analyzer.py

This class creates two threads.

Thread 1. Instantiates web server on port 8080 for displaying
          a. Current 10 second statistics of the HTTP traffic.
          
          b. Historic statistics of alarms and events.

Thread 2.  
a. Used for computing two minute average of all the 10 second hits.
   
   The sampling rate is 120//10 = 12 samples.
           
b. This thread raises an alarm if it finds that the 2 min average of hits exceeds the threshold limit.

HTTP Web server.
----------------
class TestHTTPTrafficMonitor.

Instantiates web server on port 8080 for displaying

      a. Current 10 second statistics of the HTTP traffic.

      b. Historic statistics of alarms and events.

 This class will handles any incoming request from the browser.

Unit test.
----------
class TestHTTPTrafficMonitor.
This is used to test the alarm generation and alarm clearing procedure.
