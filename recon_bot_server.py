'''TCP Server with low level programming'''


import socket, platform, os 


def main():
    SRV_ADDR = ""
    SRV_PORT =  7777


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((SRV_ADDR,SRV_PORT))
        sock.listen(1)
        conn, addr = sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                try:
                    data = conn.recv(1024)
                except:continue

                print('received:', data.decode('utf-8').strip())      

                if data.decode('utf-8').strip() == '1':
                    snd_data = platform.platform() + " " + platform.machine()  
                    conn.sendall(snd_data.encode())  
                elif data.decode('utf-8').strip() == '2':
                    req = "enter path"
                    conn.sendall(req.encode())
                    data = conn.recv(1024)
                    try:
                        filelist = os.listdir(data.decode('utf-8').strip())
                        f_pkg = ""
                        for x in filelist:
                            f_pkg += x + "\n\r"
                    except:
                        f_pkg = "WRONG PATH"
                    conn.sendall(f_pkg.encode())

                elif data.decode('utf-8').strip() == '0':
                    conn.close()
                    exit()
                else:
                    warn = "wrong selection"    
                    conn.sendall(warn.encode())

         


if __name__ == "__main__":
    main()

