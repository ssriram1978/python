import socket
from socket import getaddrinfo

HOSTS = [
'facebook.com',
'youtube.com',
]

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print(' Hostname:', name)
        print(' Aliases :', aliases)
        print(' Addresses:', addresses)
        for answer in getaddrinfo(host, 'http'):
            print(answer)

        for answer in getaddrinfo(host, 'https'):
            print(answer)

    except socket.error as msg:
        print('ERROR:', msg)
