import requests
ip_list=[]

def url_to_ip(url):
    for index in range(100):
        r = requests.get(url, stream=True)
        ip=r.raw._connection.sock.getpeername()
        try:
            index=ip_list.index(ip[0])
        except ValueError:
            print("Adding ip (%s) to the list" %(ip[0]))
            ip_list.append(ip[0])

url_to_ip("http://www.google.com")
url_to_ip("http://google.com")
url_to_ip("https://google.com")
url_to_ip("https://www.google.com")

print(ip_list)
