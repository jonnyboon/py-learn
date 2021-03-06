#!/usr/bin/env python3

import socket
from http import client
import argparse
import json

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

def chk_ressource(host,port,request_type, path, headers):   
    body=None 
    try:
        chk = client.HTTPConnection(host,port)
        chk.request(request_type,path,body, headers=headers)
        resp = chk.getresponse()
        if resp.status == 200:
            print(f"{StatColours.OKGREEN}[+] {StatColours.ENDC}", request_type, \
                " : ", " ", host," ",port, " ***")      
            #print(resp.getheaders())
            return "success"
        else:
            return None
    except Exception as e:
        print("Request failed due to: ", e)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('port', type=int)
    parser.add_argument('http_request_type', type=str)
    #parser.add_argument('path', type=str)
    #parser.add_argument('body', type=str)

    args = parser.parse_args()

    host = args.host
    port = args.port
    request_type = args.http_request_type
    path = '/admin.php'
    headers = {}
    headers ["Authorization"] = b"Basic WmFjazpNYW5hZ2VtZW50="

    #body = ''
  
    #chk_methods(host,port)
    chk_ressource(host,port,request_type,path, headers)


if __name__ == "__main__":
    main()