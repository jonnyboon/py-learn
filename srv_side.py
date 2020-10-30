'''TCP Server with low level programming'''


import socket


def main():
    SRV_ADDR = input("Pls provide IP addr for this server: ")
    SRV_PORT = int(input("whats the port for this server?: "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SRV_ADDR,SRV_PORT))
    s.listen()

    print("Server on-line")

    connection, address = s.accept()
    print('Client connected. IP-Address: ', address)

    while 1:
        data = connection.recv(1024)
        if not data: break
        connection.sendall(b'--Msg received --\n')
        print(data.decode('utf-8'))
    connection.close()


if __name__ == "__main__":
    main()

