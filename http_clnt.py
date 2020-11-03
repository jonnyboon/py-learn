import socket
from http import client

class StatColours:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def chk_methods(host,port):
    try:
        h1 = client.HTTPConnection (host,port)
        h1.request('OPTIONS','/')
        resp = h1.getresponse()
        print ("Enabled methods are: ", resp.getheader('allow'), "\n")
        print (resp.msg)
    except ConnectionRefusedError:
        print("Connection refused")

def chk_ressource(host,port,request_type):
    try:
        chk = client.HTTPConnection(host,port)
        chk.request(request_type,'/')
        print (f"[*] *** Sending ", request_type," to ", host," ",port)
        resp = chk.getresponse()
        if resp.status == 200:
            print(f"{StatColours.OKGREEN}[+] {StatColours.ENDC}", request_type, " : ", " ", host," ",port, " ***")
        else:
            print(f"{StatColours.FAIL}[-] {StatColours.ENDC}", request_type, " : ", " ", host," ",port, " ***")
        
    except Exception as e:
        print("Request failed due to: ", e)

def main():

    host = "abc.com"
    port = 80
    request_type= 'GET'

    #chk_methods(host,port)
    chk_ressource(host,port,request_type)


if __name__ == "__main__":
    main()