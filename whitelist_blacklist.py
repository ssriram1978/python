import subprocess
import re
import string
from time import sleep
from socket import getaddrinfo
from collections import defaultdict
import sys, getopt
import _socket
import dns.resolver
import dns.reversename
import logging
import threading
import time

command_to_show_acl="ip netns exec haproxy echo \"show acl #0\" | socat /var/run/haproxy/admin.sock stdio"
command_to_add_acl="ip netns exec haproxy echo \"add acl #0 %s\" | socat /var/run/haproxy/admin.sock stdio"
command_to_del_acl="ip netns exec haproxy echo \"del acl #0 %s\" | socat /var/run/haproxy/admin.sock stdio"

whitelist_file_name="/home/ssridhar/PycharmProjects/python/whitelist_blacklist.txt"

class acl_list:
    def __init__(self,listname,add_command,del_command,show_command,loglevel):
        self.acl_ipaddr=[]
        self.domain_names=[]
        self.domain_names = []
        self.add_cmd=add_command
        self.del_cmd=del_command
        self.show_cmd=show_command
        self.listname=listname
        self.domain_name_to_ip=defaultdict(list);


        numeric_level = getattr(logging,loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            logging.basicConfig(format='(%(threadName)-2s:'
                                       '%(levelname)s:'
                                       '%(asctime)s:'
                                       '%(lineno)d:'
                                       '%(filename)s:'
                                       '%(funcName)s:'
                                       '%(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p',
                                filename='whitelist_blacklist.log',
                                level=logging.DEBUG)
        else:
            logging.basicConfig(format='(%(threadName)-2s'
                                       '%(levelname)s:'
                                       '%(asctime)s:'
                                       '%(lineno)d:'
                                       '%(filename)s:'
                                       '%(funcName)s:'
                                       '%(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p',
                                filename='whitelist_blacklist.log',
                                level=numeric_level)

        while True:
            try:
                #read all the acl ip address from HAPROXY.
                self.perform_acl_read()
                #open the file and read all the domain names from the file and convert it to IPaddresses.
                self.read_list()
                #clean up the domain name list
                self.cleanup_domain_name_dict()
                #match the acl with the ip addresses.
                self.refresh_acl()
                logging.debug("sleeping for 0.2 seconds...")
                sleep(0.2)
            except KeyboardInterrupt:
                break
            except:
                sys_exec_info=sys.exc_info()[0]
                logging.error("Unexpected error:%s" %(sys_exec_info))

    def perform_acl_read(self):
        self.acl_ipaddr=[]
        completed = subprocess.run([self.show_cmd],
                                   check=True,
                                   shell=True,
                                   stdout=subprocess.PIPE)
        logging.debug('returncode:', completed.returncode)
        formated_string=completed.stdout.decode('utf-8')
        aclist=formated_string.strip().split('\n')
        logging.debug("\nself.aclist=")
        logging.debug(aclist)
        for current_acl in aclist:
            temp_list = str(current_acl).split(' ')
            if len(temp_list) >= 2:
                self.acl_ipaddr.append(temp_list[1])
        logging.debug("\nself.acl_ipaddr=")
        logging.debug(print(self.acl_ipaddr))

    def read_list(self):
        #self.domain_name_to_ip={}
        self.domain_names = []
        with open(self.listname, "r") as ins:
            for line in ins:
                domain_name=str(line.strip())
                if len(domain_name) > 0:
                    self.add_doman_name_to_list(domain_name)
                    self.convert_dnsname_to_ip(domain_name)
        logging.debug("\nself.dictionary_elements=")
        logging.debug(self.domain_name_to_ip)
        logging.debug("\nself.domain_names=")
        logging.debug(self.domain_names)

        ins.close()

    def add_doman_name_to_list(self,domain_name):
        if len(domain_name) > 0:
            matchFound = False
            for name in domain_name:
                if str(name) == str(domain_name):
                    matchFound = True
                    break
            if matchFound == False:
                self.domain_names.append(domain_name)

    def convert_dnsname_to_ip(self,dnsname):
        # expand hostname into dict of ip addresses
        for answer in getaddrinfo(dnsname, 80):
            ipa = str(answer[4][0])
            ip_list=self.domain_name_to_ip[dnsname]

            if ip_list == None:
                ip_list = ipa
            else:
                #check if the ip address is already there in the list
                matchFound=False
                for ip_addr in ip_list:
                    if str(ip_addr) in str(ipa):
                        matchFound=True
                        break
                if matchFound == False:
                    logging.debug("For domain name (%s), appending IP address (%s) to the list." %(dnsname,ipa))
                    ip_list.append(ipa)
            #assign back the ip_list back to the dictionary.
            self.domain_name_to_ip[dnsname]=ip_list

    def cleanup_domain_name_dict(self):
        for domain_name_dict, ipaddr_list in self.domain_name_to_ip.items():
            match_found = False
            for domain_name in self.domain_names:
                # for every domain_name_dict search for the domain name in the list.
                if domain_name == domain_name_dict:
                    match_found=True
                    break;
            if match_found == False:
                #Delete this domain name from the dictionary.
                self.domain_name_to_ip.pop(domain_name_dict)


    def delete_acl_ip(self,acl_ip):
        final_del_acl = self.del_cmd % (acl_ip)
        logging.debug(final_del_acl)
        completed = subprocess.run([final_del_acl],
                                   check=True,
                                   shell=True,
                                   stdout=subprocess.PIPE)
        logging.debug('Deleted %s from acl.' % (acl_ip))

    def add_acl_ip(self,acl_ip):
        final_add_acl = self.add_cmd % (acl_ip)
        logging.debug(final_add_acl)
        completed = subprocess.run([final_add_acl],
                                   check=True,
                                   shell=True,
                                   stdout=subprocess.PIPE)
        logging.debug('Added %s to acl.' %(acl_ip))

    def refresh_acl(self):
        #add the new IP address provided by DNS resolution.
        for name, ipaddr_list in self.domain_name_to_ip.items():
            for ipaddr_in in ipaddr_list:
                match_found = False
                for ipaddr_acl in self.acl_ipaddr:
                    # for every item search for the item in the acl list.
                    if ipaddr_in in ipaddr_acl:
                        match_found=True
                        break;
                if match_found == False:
                    #add this new ip to the list
                    self.add_acl_ip(ipaddr_in)

        #delete all those IP addresses that are stale in the acl_list
        for ipaddr_acl in self.acl_ipaddr:
            match_found = False
            for domain_name, ipaddr_list in self.domain_name_to_ip.items():
                for ipaddr_in in ipaddr_list:
                    # for every item search for the item in the acl list.
                    if ipaddr_in in ipaddr_acl:
                        match_found = True
                        break;
                if match_found == True:
                    break;
            if match_found == False:
                # del this ip from acl because this is stale.
                self.delete_acl_ip(ipaddr_acl)


    def perform_match(self):
        for ipaddr_in in self.domain_name_to_ip:
            match_found=False
            #for every item search for the item in the acl list.
            for ipaddr_acl in self.acl_ipaddr:
                if ipaddr_in in ipaddr_acl:
                    logging.debug("match found for "+ ipaddr_in)
                    match_found=True
                    break
            if match_found == True:
                #do nothing
                logging.debug("skipping this ip address %s because it is already in the list" %(ipaddr_in))
            else:
                #add this new item to the acl list.
                logging.debug("going to add this item %s to this list" %(ipaddr_in))
                final_add_acl=self.add_cmd %(ipaddr_in)
                logging.debug(final_add_acl)
                completed = subprocess.run([final_add_acl],
                                           check=True,
                                           shell=True,
                                           stdout=subprocess.PIPE)
                logging.debug('returncode:', completed.returncode)


debug = ''
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"h:d:",["debug="])
    except getopt.GetoptError:
        print('whitelist_blacklist.py -d <debug>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('whitelist_blacklist.py -d <debug>')
            sys.exit()
        elif opt in ("-d"):
            debug = arg
            print("debug %s" %(debug))

    file_command=acl_list(whitelist_file_name,
                      command_to_add_acl,
                      command_to_del_acl,
                      command_to_show_acl,debug)


if __name__ == "__main__":
   main(sys.argv[1:])