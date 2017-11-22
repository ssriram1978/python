import subprocess
import re
import string
from time import sleep
from socket import getaddrinfo
from collections import defaultdict
import sys
import _socket
import dns.resolver
import dns.reversename


command_to_show_acl="ip netns exec haproxy echo \"show acl #0\" | socat /var/run/haproxy/admin.sock stdio"
command_to_add_acl="ip netns exec haproxy echo \"add acl #0 %s\" | socat /var/run/haproxy/admin.sock stdio"
command_to_del_acl="ip netns exec haproxy echo \"del acl #0 %s\" | socat /var/run/haproxy/admin.sock stdio"

whitelist_file_name="whitelist_blacklist.txt"

class acl_list:
    def __init__(self,listname,add_command,del_command,show_command):
        self.acl_ipaddr=[]
        self.domain_names=[]
        self.domain_names = []
        self.add_cmd=add_command
        self.del_cmd=del_command
        self.show_cmd=show_command
        self.listname=listname
        self.domain_name_to_ip=defaultdict(list);

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
                print("sleeping for 0.2 seconds...")
                sleep(0.2)
            except KeyboardInterrupt:
                break
            except:
                print("Unexpected error:", sys.exc_info()[0])

    def perform_acl_read(self):
        self.acl_ipaddr=[]
        completed = subprocess.run([self.show_cmd],check=True,shell=True,stdout=subprocess.PIPE)
        #print('returncode:', completed.returncode)
        formated_string=completed.stdout.decode('utf-8')
        aclist=formated_string.strip().split('\n')
        #print("\nself.aclist=")
        #print(aclist)
        for current_acl in aclist:
            temp_list = str(current_acl).split(' ')
            if len(temp_list) >= 2:
                self.acl_ipaddr.append(temp_list[1])
        print("\nself.acl_ipaddr=")
        print(self.acl_ipaddr)

    def read_list(self):
        #self.domain_name_to_ip={}
        self.domain_names = []
        with open(self.listname, "r") as ins:
            for line in ins:
                domain_name=str(line.strip())
                if len(domain_name) > 0:
                    self.add_doman_name_to_list(domain_name)
                    self.convert_dnsname_to_ip(domain_name)
        print("\nself.dictionary_elements=")
        print(self.domain_name_to_ip)
        #print("\nself.domain_names=")
        #print(self.domain_names)

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
                    print("For domain name (%s), appending IP address (%s) to the list." %(dnsname,ipa))
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
        print(final_del_acl)
        completed = subprocess.run([final_del_acl],check=True,shell=True,stdout=subprocess.PIPE)
        print('Deleted %s from acl.' % (acl_ip))

    def add_acl_ip(self,acl_ip):
        final_add_acl = self.add_cmd % (acl_ip)
        print(final_add_acl)
        completed = subprocess.run([final_add_acl],check=True,shell=True,stdout=subprocess.PIPE)
        print('Added %s to acl.' %(acl_ip))

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
                    print("match found for "+ ipaddr_in)
                    match_found=True
                    break
            if match_found == True:
                #do nothing
                print("skipping this ip address %s because it is already in the list" %(ipaddr_in))
            else:
                #add this new item to the acl list.
                print("going to add this item %s to this list" %(ipaddr_in))
                final_add_acl=self.add_cmd %(ipaddr_in)
                print(final_add_acl)
                completed = subprocess.run([final_add_acl],check=True,shell=True,stdout=subprocess.PIPE)
                print('returncode:', completed.returncode)


file_command=acl_list(whitelist_file_name,command_to_add_acl,command_to_del_acl,command_to_show_acl)
