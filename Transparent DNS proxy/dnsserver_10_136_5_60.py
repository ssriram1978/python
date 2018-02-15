import sys
from socket import *
from dnslib import *
import datetime
import sys
import time
import socket
import fcntl
from scapy.all import *
import io
import logging

whitelist_blacklist_file_name="/home/istguser1/whitelist_blacklist2.txt"
dns_query_names="/home/istguser1/dnsq.txt"

PORT=53
BUFSIZE = 1024
IP_TRANSPARENT=19
IP_FREEBIND=15
IP_BINDANY=24
MAC_OF_BBI_NEXT_HOP="e4:d3:f1:fc:75:00"
MAC_OF_DNS_CONT="60:00:00:00:00:00"

def match_dns_query_name_with_whitelist_blacklist(data):
    request = DNSRecord.parse(data)
    print("request=%s" %(str(request)))
    qname = str(request.q.qname).strip('.')
    print("qname=" + qname)
    #qtype = request.q.qtype

    if qname in open(whitelist_blacklist_file_name).read():
        success = 0
        q = DNSRecord.question(qname)
        reply = q.reply()
        if success == 1 :
            reply = DNSRecord(DNSHeader(id=request.header.id, opcode=2, rcode=5, qr=1, aa=1, ra=0), q=request.q)
            denied_string="VISP: Sorry, this website is restricted by your admin."
            #reply.add_answer(RR(rname=qname, rtype=2, rclass=1, ttl=TTL, rdata=denied_string))
            reply.add_answer(RR(qname, QTYPE.SOA, rdata=SOA(denied_string)))
        else:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("1.2.3.4"), ttl=60))
        reply.header.id = request.header.id
        #print("request.header.id=%d\n" %(request.header.id))
        #print("reply.header.id=%d\n" %(reply.header.id))
        print("---- Reply:%s\n" %(reply))
        return reply.pack()
    else :
        return None

def match_dns_query_name_with_whitelist_blacklist2(data):
    request = DNSRecord.parse(data)
    print("request=%s" %(str(request)))
    qname = str(request.q.qname).strip('.')
    print("qname=" + qname)
    #qtype = request.q.qtype

    if qname in open(whitelist_blacklist_file_name).read():
        success = 0
        q = DNSRecord.question(qname)
        reply = q.reply()
        if success == 1 :
            reply = DNSRecord(DNSHeader(id=request.header.id, opcode=2, rcode=5, qr=1, aa=1, ra=0), q=request.q)
            denied_string="VISP: Sorry, this website is restricted by your admin."
            #reply.add_answer(RR(rname=qname, rtype=2, rclass=1, ttl=TTL, rdata=denied_string))
            reply.add_answer(RR(qname, QTYPE.SOA, rdata=SOA(denied_string)))
        else:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("1.2.3.4"), ttl=60))
        reply.header.id = request.header.id
        #print("request.header.id=%d\n" %(request.header.id))
        #print("reply.header.id=%d\n" %(reply.header.id))
        print("---- Reply:%s\n" %(reply))
        return reply.pack()
    else :
        return None

def server():
    s = socket.socket(AF_INET, SOCK_DGRAM,socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, IP_TRANSPARENT, 1)
    s.setsockopt(socket.IPPROTO_IP, IP_FREEBIND, 1)
    s.setsockopt(socket.IPPROTO_IP, IP_BINDANY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(('', PORT))
    #fcntl.ioctl(s, SIO_RCVALL, 1)
    #s.setsockopt(socket.SIO_RCVALL, socket.RCVALL_ON)
    #s.setsockopt(socket.IPPROTO_IP,socket.SIO_RCVALL,1)

    print('udp echo server ready')
    while 1:
        data, addr = s.recvfrom(BUFSIZE)
        print('server received %r from %r' %(data, addr))
        dns_response = match_dns_query_name_with_whitelist_blacklist(data)
        if dns_response == None:
            # just allow this DNS to pass through
            print("dns response is none.\n")
            s.send(data,addr)
        else:
            s.sendto(dns_response,addr)



def sniff_packet(pkt):
    #logging.debug("Rcvd pkt:")
    #logging.debug(hexdump(pkt))

    if (pkt[Ether].dst != MAC_OF_DNS_CONT):
        #logging.debug("Discarding this packet because dest mac does not match this host.")
        return

    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
    if UDP in pkt:
        udp_sport = pkt[UDP].sport
        udp_dport = pkt[UDP].dport

        #try:
        if 1:
            if udp_dport == 53:
                #logging.debug(" IP src " + str(ip_src) + " UDP sport " + str(udp_sport))
                #logging.debug(" IP dst " + str(ip_dst) + " UDP dport " + str(udp_dport))
                #print("pkt[UDP].payload=%s\n" % (pkt[UDP].payload))
                request = DNSRecord.parse(bytes(pkt[UDP].payload))

                #logging.debug("request=%s\n" % (str(request)))
                qname = str(request.q.qname).strip('.')
                #logging.debug("Domain name got from the DNS request =%s\n"%(qname))
                #logging.debug("request.header.id=%d\n" % (request.header.id))

                open(dns_query_names,'a+').write(qname + '\n')

                match_found=False

                dns_reject=False
                dns_redirect_to_static_webpage=True

                for line in open(whitelist_blacklist_file_name) :
                    line=line.strip('\n')                    
                    if line in qname:
                        DNS_resp=DNS()
                        DNS_resp.id=request.header.id
                        DNS_resp.qr=1
                        DNS_resp.aa=1
                        DNS_resp.ra=1
                        #DNS_resp.opcode = 2
                        DNS_resp.rcode=0
                        #DNS_resp.rcode=5
                        DNS_resp.qd=DNSQR(qname=qname)
                        #DNS_resp.an=DNSRR(rrname=qname,type=16,rclass=1,ttl=3600,rdata='From VISP: Content restricted.')
                        #DNS_resp.an=DNSRR(rrname=qname,type=1,rclass=1,ttl=3600,rdata='151.101.129.67')
                        if dns_reject ==True:
                            DNS_resp.an = DNSRR(rrname=qname, type=16, rclass=1, ttl=3600,
                                                rdata='From VISP: Content restricted.')
                            logging.debug(
                                "line=%s and qname=%s match.Composing and sending DNS Reject (%s).\n"
                                %(line, qname, ip_addr))
                        elif dns_redirect_to_static_webpage == True:
                            ip_addr="10.2.40.164"
                            DNS_resp.an=DNSRR(rrname=qname,type="A",rclass=1,ttl=120,rdata=ip_addr)
                            logging.debug(
                            "line=%s and qname=%s match.Composing and sending DNS response "
                            "pointing to a web server (%s).\n"
                            %(line, qname, ip_addr))

                        #response = DNSRecord.parse(bytes(DNS_resp))
                        dns_response_packet = Ether(src=pkt[Ether].dst,dst=pkt[Ether].src) /\
                                          IP(src=str(ip_dst), dst=str(ip_src)) / \
                                          UDP(sport=udp_dport, dport=udp_sport) / \
                                          DNS_resp

                        #logging.debug(hexdump(dns_response_packet))
                        sendp(dns_response_packet,loop=False,realtime=True,iface='DNSCONT',verbose=False)
                        match_found=True
                        break

                if match_found == False:
                    #leave the packet untouched.
                    dns_req = Ether(src=pkt[Ether].src,dst=MAC_OF_BBI_NEXT_HOP)/ \
                                  IP(src=str(pkt[IP].src), dst=str(pkt[IP].dst)) / \
                                  UDP(sport=pkt[UDP].sport, dport=pkt[UDP].dport) / \
                                  bytes(pkt[UDP].payload)

                    logging.debug("Composing and forwarding DNS request for domain name =%s to the original dest.\n" %(qname))
                    #logging.debug(hexdump(dns_req))
                    sendp(dns_req,loop=False,realtime=True,iface='DNSCONT',verbose=False)
            else:
                #leave the packet untouched.
                #logging.debug("Received a packet with UDP sport=%s and UDP dport=%s.\n" %(str(udp_sport),str(udp_dport)))
                orig_request = Ether(src=pkt[Ether].src, dst=MAC_OF_BBI_NEXT_HOP) / \
                            IP(src=str(pkt[IP].src), dst=str(pkt[IP].dst)) / \
                            UDP(sport=pkt[UDP].sport, dport=pkt[UDP].dport) / \
                            bytes(pkt[UDP].payload)
                #logging.debug(hexdump(orig_request))
                sendp(orig_request, loop=False, realtime=True, iface='DNSCONT',verbose=False)


        #except:
        #    sys_exec_info = sys.exc_info()[0]
        #    logging.error("Unexpected error:%s" % (sys_exec_info))

logging.basicConfig(format='(%(threadName)-2s:'
                                       '%(levelname)s:'
                                       '%(asctime)s:'
                                       '%(lineno)d:'
                                       '%(filename)s:'
                                       '%(funcName)s:'
                                       '%(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p',
                                filename='dns_server_10_136_5_60.log',
                                level=logging.DEBUG)

sniff(iface='DNSCONT',filter='udp and port 53',prn=sniff_packet,store=False)
#sniff(iface='DNSCONT',filter='udp',prn=sniff_packet,store=False)


#server()