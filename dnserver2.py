# coding=utf-8

import datetime
import sys
import time
import threading
import traceback
import socketserver
from dnslib import *

whitelist_blacklist_file_name="/home/ssridhar/PycharmProjects/python/whitelist_blacklist.txt"

class DomainName(str):
    def __getattr__(self, item):
        return DomainName(item + '.' + self)

TTL = 60 * 5
PORT = 53


def match_dns_query_name_with_whitelist_blacklist(data):
    request = DNSRecord.parse(data)


    print("request=%s" %(str(request)))
    qname = str(request.q.qname).strip('.')

    print("qname=" + qname)
    #qtype = request.q.qtype

    if qname in open(whitelist_blacklist_file_name).read():
        reply = DNSRecord(DNSHeader(id=request.header.id, opcode=2, rcode=5, qr=1, aa=1, ra=0), q=request.q)
        denied_string="VISP: Sorry, this website is restricted by your admin."
        #reply.add_answer(RR(rname=qname, rtype=2, rclass=1, ttl=TTL, rdata=denied_string))
        reply.add_answer(RR(qname, QTYPE.SOA, rdata=SOA(denied_string)))
        print("---- Reply:%s\n" %(reply))
        return reply.pack()
    else :
        return None


class BaseRequestHandler(socketserver.BaseRequestHandler):

    def get_data(self):
        raise NotImplementedError

    def send_data(self, data):
        raise NotImplementedError

    def handle(self):
        now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("\n\n%s request %s (%s %s):" % (self.__class__.__name__[:3], now, self.client_address[0],
                                               self.client_address[1]))
        try:
            data = self.get_data()
            print("Received a request with len%d" %(len(data)))
            #print(str(data.encode('hex')))  # repr(data).replace('\\x', '')[1:-1]
            dns_response=match_dns_query_name_with_whitelist_blacklist(data)
            if dns_response == None:
                #just allow this DNS to pass through
                self.send_data(self.get_data())
            else:
                self.send_data(dns_response)
        except Exception:
            traceback.print_exc(file=sys.stderr)

class UDPRequestHandler(BaseRequestHandler):

    def get_data(self):
        return self.request[0].strip()

    def send_data(self, data):
        return self.request[1].sendto(data, self.client_address)


if __name__ == '__main__':
    print("Starting nameserver...")

    servers = [
        socketserver.ThreadingUDPServer(('127.0.0.1', PORT), UDPRequestHandler),
    ]
    for s in servers:
        thread = threading.Thread(target=s.serve_forever)  # that thread will start one more thread for each request
        thread.daemon = True  # exit the server thread when the main thread terminates
        thread.start()
        print("%s server loop running in thread: %s" % (s.RequestHandlerClass.__name__[:3], thread.name))

    try:
        while 1:
            time.sleep(1)
            sys.stderr.flush()
            sys.stdout.flush()

    except KeyboardInterrupt:
        pass
    finally:
        for s in servers:
            s.shutdown()