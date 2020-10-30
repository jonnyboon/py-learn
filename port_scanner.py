'''TCP Server with low level programming'''


import socket


def main():
    SRV_ADDR = input("Pls provide target IP addr: ")
    SRV_PORT_RNG = input("whats the port range (ex 1-1024)?: ")

    #extract port range
    init_port = int(SRV_PORT_RNG.split('-')[0])
    fin_port = int(SRV_PORT_RNG.split('-')[1])


    for port in range(init_port, fin_port+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_stat = s.connect_ex((SRV_ADDR,port))

        if (conn_stat == 0):
            print("[+] OPEN port: ", port)
        else:
            print("----[-] CLOSED port: ", port)

        s.close()


if __name__ == "__main__":
    main()

