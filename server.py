import socket
import threading
import forcebytes
connections = []
names = []
names.append('Ivan')
nameslen = len(names)
def multi_client(conn):
                print(f"Connected by {addr}")
                conn.sendall(str.encode(str(nameslen)))
                for w in range(len(names)):
                        conn.sendall(str.encode(names[w]))
                names.append(conn.recv(1024).decode("ascii"))
                print(names)
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
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
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