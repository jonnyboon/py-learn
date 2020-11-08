'''TCP Server with low level programming'''


import socket
import argparse

class StatColours:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def scan_ports(host,port_init,fpor_fin):
    for port in range(port_init, fpor_fin+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_stat = s.connect_ex((host,port))

        if (conn_stat == 0):
            print(f"{StatColours.OKGREEN}[+] {StatColours.ENDC}", \
                " : ", " ", host," ",port, " ***")
        else:
            continue

        s.close()    



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('port_rng', type=str)

    args = parser.parse_args()

    SRV_ADDR = args.host
    SRV_PORT_RNG = args.port_rng

    #extract port range
    init_port = int(SRV_PORT_RNG.split('-')[0])
    fin_port = int(SRV_PORT_RNG.split('-')[1])

    scan_ports(SRV_ADDR, init_port,fin_port)


if __name__ == "__main__":
    main()

