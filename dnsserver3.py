import sys
from socket import *
from dnslib import *
import datetime
import sys
import time
import socket
import fcntl
from scapy.all import *

whitelist_blacklist_file_name="/home/ssridhar/PycharmProjects/python/whitelist_blacklist.txt"

PORT=53
BUFSIZE = 1024
IP_TRANSPARENT=19
IP_FREEBIND=15
IP_BINDANY=24
MAC_OF_BBI_NEXT_HOP="44:03:a7:11:98:81"
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
    print("Rcvd pkt:")
    print(hexdump(pkt))

    if (pkt[Ether].dst != MAC_OF_DNS_CONT):
        print("Discarding this packet because dest mac does not match this host.")
        return

    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
    if UDP in pkt:
        udp_sport = pkt[UDP].sport
        udp_dport = pkt[UDP].dport

        try:
            if udp_dport == 53:
                print(" IP src " + str(ip_src) + " UDP sport " + str(udp_sport))
                print(" IP dst " + str(ip_dst) + " UDP dport " + str(udp_dport))
                #print("pkt[UDP].payload=%s\n" % (pkt[UDP].payload))
                request = DNSRecord.parse(bytes(pkt[UDP].payload))

                print("request=%s\n" % (str(request)))
                qname = str(request.q.qname).strip('.')
                print("qname=%s\n"%(qname))
                print("request.header.id=%d\n" % (request.header.id))

                if qname in open(whitelist_blacklist_file_name).read():
                    DNS_resp=DNS()
                    DNS_resp.id=request.header.id
                    DNS_resp.qr=1
                    DNS_resp.opcode = 2
                    DNS_resp.rcode=5
                    DNS_resp.qd=DNSQR(qname=qname)
                    DNS_resp.an=DNSRR(rrname=qname,type=16,ttl=3600,rdata='Not allowed.')

                    response = DNSRecord.parse(bytes(DNS_resp))
                    dns_response_packet = Ether(src=pkt[Ether].dst,dst=pkt[Ether].src) /\
                                          IP(src=str(ip_dst), dst=str(ip_src)) / \
                                          UDP(sport=udp_dport, dport=udp_sport) / \
                                          DNS_resp
                    print("Composing and sending DNS response pkt:")
                    print(hexdump(dns_response_packet))
                    sendp(dns_response_packet,loop=False,realtime=True,iface='DNSCONT',verbose=True)
                else:
                    #leave the packet untouched.
                        dns_req = Ether(src=pkt[Ether].src,dst=MAC_OF_BBI_NEXT_HOP)/ \
                                  IP(src=str(pkt[IP].src), dst=str(pkt[IP].dst)) / \
                                  UDP(sport=pkt[UDP].sport, dport=pkt[UDP].dport) / \
                                  bytes(pkt[UDP].payload)

                        print("Composing and forwarding DNS request to the original dest.\n")
                        print(hexdump(dns_req))
                        sendp(dns_req,loop=False,realtime=True,iface='DNSCONT',verbose=True)


            else:
                #leave the packet untouched.
                print("Received a packet with UDP sport=%s and UDP dport=%s.\n" %(str(udp_sport),str(udp_dport)))
                orig_request = Ether(src=pkt[Ether].src, dst=MAC_OF_BBI_NEXT_HOP) / \
                            IP(src=str(pkt[IP].src), dst=str(pkt[IP].dst)) / \
                            UDP(sport=pkt[UDP].sport, dport=pkt[UDP].dport) / \
                            bytes(pkt[UDP].payload)
                print(hexdump(orig_request))
                sendp(orig_request, loop=False, realtime=True, iface='DNSCONT', verbose=True)


        except:
            sys_exec_info = sys.exc_info()[0]
            logging.error("Unexpected error:%s" % (sys_exec_info))



sniff(iface='DNSCONT',filter='udp and port 53',prn=sniff_packet,store=False)
#sniff(iface='DNSCONT',filter='udp',prn=sniff_packet,store=False)

#server()
