from socket import *
import threading
connections = []

def multi_client(conn):
                print(f"Connected by {addr}")
                while True:
                        try:
                                data = conn.recv(1024)
                        except Exception:
                                return
                        print(f"Server received {data!r}")
                        for c in connections:
                                if c != conn:                              
                                        try:
                                                c.sendall(data)
                                        except Exception:
                                                connections.remove(c)
                        if not data:
                                return
                

        
HOST = "192.168.68.102"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)
on = 0
with socket(AF_INET, SOCK_STREAM) as s: 
        s.bind((HOST, PORT))
        while True:
                if on == 0:
                        print("I'm On")
                        on = 1
                s.listen()
                conn, addr = s.accept()
                connections.append(conn)
                thread = threading.Thread(target=multi_client, args=[conn])
                thread.start()
                