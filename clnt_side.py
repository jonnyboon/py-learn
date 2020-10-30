'''TCP Server with low level programming'''


import socket


def main():
    SRV_ADDR = input("Pls provide IP addr for this server: ")
    SRV_PORT = int(input("whats the port for this server?: "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SRV_ADDR,SRV_PORT))

    print("Connection to server stablished on ", SRV_ADDR, " ", SRV_PORT)

    message = input("What is your message? ")

    s.sendall(message.encode())
    s.close()


if __name__ == "__main__":
    main()

