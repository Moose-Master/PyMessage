import socket
import threading
import DefOther
import random
connections = []
names = ['Sever','Admin','Ivan']
def multi_client(conn):
                print(f"Connected by {addr}")
                name = "Some User"
                rand = random.randint(92,97)
                
                while True:
                        try:
                                msglen = int.from_bytes(DefOther.fr(conn,4),byteorder='big')
                                msgtyp = DefOther.fr(conn,1).decode('ascii')
                                if msgtyp == 'M':
                                        data = DefOther.fr(conn,msglen).decode('utf-8')
                                        print('\033[' + str(rand)  + "m" + name + ": " + data)
                                        for c in connections:
                                                if c != conn:                              
                                                        try:
                                                                msg = str.encode('\033[' + str(rand)  + "m" + name + ": " + data, "utf-8")
                                                                c.sendall(len(msg).to_bytes(4,'big'))
                                                                c.sendall(str.encode("M",'ascii'))
                                                                c.sendall(msg)
                                                        except Exception:
                                                                names.remove(name)
                                                                connections.remove(c)
                                        if not data:
                                                return
                                elif msgtyp == '^':
                                        name = DefOther.fr(conn,msglen).decode('ascii')
                                        n_taken = 0                                       
                                        for i in range(len(names)):
                                                if name.casefold() == names[i].casefold():
                                                        print('Match')
                                                        s.sendall((len('That Name is Taken Try Again')).to_bytes(4,'big'))
                                                        s.sendall(str.encode("^",'ascii'))
                                                        s.sendall(str.encode('That Name is Taken Try Again','utf-8'))
                                                        n_taken = 1
                                        if name == "AllKnowing":
                                                name = 'Admin'
                                        elif name == "FullControl":
                                                name = 'Sever'
                                        elif name== "TrueOwner":
                                                name = "Ivan"
                                        if n_taken == 0:
                                                names.append(name)
                                                print(name + " Joined")
                                                for c in connections:
                                                        if c != conn:                              
                                                                try:
                                                                        c.sendall((len(name + " Joined")).to_bytes(4,'big'))
                                                                        c.sendall(str.encode("M",'ascii'))
                                                                        c.sendall(str.encode(name + " Joined",'utf-8'))
                                                                except Exception:
                                                                        connections.remove(c)
                                elif msgtyp == '*':
                                        print()

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