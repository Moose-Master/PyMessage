import socket
import threading
import forcebytes
connections = []
def multi_client(conn):
                print(f"Connected by {addr}")
                name = "Some User"
                while True:
                        try:
                                msglen = int.from_bytes(forcebytes.fr(conn,4),byteorder='big')
                                msgtyp = forcebytes.fr(conn,1).decode('ascii')
                                if msgtyp == 'M':
                                        data = forcebytes.fr(conn,msglen).decode('utf-8')
                                        print(data)
                                        for c in connections:
                                                if c != conn:                              
                                                        try:
                                                                c.sendall((len(name + ": " + data)).to_bytes(4,'big'))
                                                                c.sendall(str.encode(name + ": " + data,'utf-8'))
                                                        except Exception:
                                                                connections.remove(c)
                                        if not data:
                                                return
                                else:
                                        name = forcebytes.fr(conn,msglen).decode('ascii')
                        except Exception:
                                return
HOST = "192.168.68.102" 
PORT = 65433
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