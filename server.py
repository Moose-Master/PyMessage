import socket
import threading
import DefOther
import random
ban_list = []
connections: list[tuple[socket.socket, str]] = []
names = ['Server','Admin','Ivan','Belle']
def multi_client(conn):
        for i in range(len(ban_list)):
                print(ban_list[i])
                if str(addr[0]) == str(ban_list[i]):
                        print("Banned!")
                        s.close
                        return
        print(f"Connected by {addr}")
        name = "Some User"
        rand_0 = random.randint(0,2)
        if rand_0 == 1:
                rand = random.randint(91,97)
        else:
                rand = random.randint(31,37)
        while True:
                try:
                        msglen = int.from_bytes(DefOther.fr(conn,4),byteorder='big')
                        msgtyp = DefOther.fr(conn,1).decode('ascii')
                        if msgtyp == 'M':
                                data = DefOther.fr(conn,msglen).decode('utf-8')
                                print('\033[' + str(rand)  + "m" + name + ": " + data)
                                for c, cname in connections:
                                        if c != conn:                              
                                                try:
                                                        msg = str.encode('\033[' + str(rand)  + "m" + name + ": " + data, "utf-8")
                                                        c.sendall(len(msg).to_bytes(4,'big'))
                                                        c.sendall(str.encode("M",'ascii'))
                                                        c.sendall(msg)
                                                except Exception:
                                                        connections.remove((c,cname))
                                if not data:
                                        return
                        elif msgtyp == '^':
                                name = DefOther.fr(conn,msglen).decode('ascii')
                                n_taken = False                                       
                                for i in range(len(names)):
                                        if name.casefold() == names[i].casefold():
                                                print('Match')
                                                s.sendall((len('That Name is Taken Try Again')).to_bytes(4,'big'))
                                                s.sendall(str.encode("^",'ascii'))
                                                s.sendall(str.encode('That Name is Taken Try Again','utf-8'))
                                                n_taken = True
                                for c, cname in connections:
                                        if cname.casefold() == name.casefold():
                                                print('Match')
                                                s.sendall((len('')).to_bytes(4,'big'))
                                                s.sendall(str.encode("^",'ascii'))
                                                n_taken = True
                                if name.casefold() == "AllKnowing".casefold():
                                        name = 'Admin'
                                elif name.casefold() == "FullControl".casefold():
                                        name = 'Server'
                                elif name.casefold() == "TrueOwner".casefold():
                                        name = "Ivan"
                                elif name.casefold() == "Lady Wind Master".casefold():
                                        name = 'Belle'
                                if n_taken == False:
                                        print(name + " Joined")
                                        for c,cname in connections:
                                                if c != conn:                              
                                                        try:
                                                                c.sendall((len(name + " Joined")).to_bytes(4,'big'))
                                                                c.sendall(str.encode("M",'ascii'))
                                                                c.sendall(str.encode(name + " Joined",'utf-8'))
                                                        except Exception:
                                                                connections.remove((c,cname))
                                for i in range(len(connections)):
                                        if connections[i][0] == conn:
                                                connections[i] = (conn, name)
                                                break
                        elif msgtyp == '*':
                                lon = ''.join(str(x[1] + ", ") for x in connections)
                                print(lon)
                                for c, cname in connections:
                                        if c == conn:                              
                                                try:
                                                        msg = str.encode('\033[' + str(rand)  + "m" + "Server: " + lon, "utf-8")
                                                        c.sendall(len(msg).to_bytes(4,'big'))
                                                        c.sendall(str.encode("M",'ascii'))
                                                        c.sendall(msg)
                                                except Exception:
                                                        connections.remove((c,cname))
                        elif msgtyp == '&' and (name == "Ivan" or name == "Admin" or name == "Server"):
                                data = int(DefOther.fr(conn,msglen).decode('utf-8'))
                                print("Kicking " + str(connections[data][1]))
                                c = connections[data][0]
                                try:
                                        c.sendall(len("").to_bytes(4,'big'))
                                        c.sendall(str.encode("&",'ascii'))
                                        print("Kicked " + connections[data][1])
                                        connections.remove((connections[data]))
                                except Exception:
                                                connections.remove((connections[data]))
                        elif msgtyp == '#' and (name == "Ivan" or name == "Admin" or name == "Server"):
                                data = int(DefOther.fr(conn,msglen).decode('utf-8'))
                                c = connections[data][0]
                                try:
                                        ban_list.append(str(addr[0]))
                                        c.sendall(len("").to_bytes(4,'big'))
                                        c.sendall(str.encode("&",'ascii'))
                                        print("Ip Baned " + connections[data][1])
                                        connections.remove((connections[data]))
                                        print(addr[0])
                                except Exception:
                                        connections.remove((connections[data]))
                        elif msgtyp == '@':
                                data = DefOther.fr(conn,msglen).decode('utf-8')
                                print(data)
                                amount = len(data)
                                pm_names = []
                                la = -1
                                print("Recived PM, Procesing")
                                for i in range(amount):
                                        if data[i] == '@':
                                                pm_names.append(data[(la+1):i])
                                                la = i
                                                print(pm_names)
                                                print(data)
                                data = data[(la+1):]
                                print(data)
                                for i in range(len(pm_names)):
                                        for c, cname in connections:
                                                if cname == pm_names[i]:
                                                        try:
                                                                msg = str.encode('\033[' + str(rand)  + "m" + name +": " + data, "utf-8")
                                                                c.sendall(len(msg).to_bytes(4,'big'))
                                                                c.sendall(str.encode("M",'ascii'))
                                                                c.sendall(msg)
                                                        except Exception:
                                                                connections.remove((c,cname))
                        elif msgtyp == '$':
                                data = DefOther.fr(conn,msglen).decode('utf-8')
                                print(data)
                                amount = len(data)
                                exm_names = []
                                ld = -1
                                print("Recived EXM, Procesing")
                                for i in range(amount):
                                        if data[i] == '$':
                                                exm_names.append(data[(ld+1):i])
                                                ld = i
                                                print(exm_names)
                                                print(data)
                                data = data[(ld+1):]
                                print(data)
                                for i in range(len(exm_names)):
                                        for c, cname in connections:
                                                if cname != exm_names[i]:
                                                        try:
                                                                msg = str.encode('\033[' + str(rand)  + "m" + name +": " + data, "utf-8")
                                                                c.sendall(len(msg).to_bytes(4,'big'))
                                                                c.sendall(str.encode("M",'ascii'))
                                                                c.sendall(msg)
                                                        except Exception:
                                                                connections.remove((c,cname))
                except Exception:
                        return
HOST = "0.0.0.0" 
PORT = 21894
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.bind((HOST, PORT))
        print("I'm On")
        while True:
                s.listen()
                conn, addr = s.accept()
                connections.append((conn, "anonymous"))
                thread = threading.Thread(target=multi_client, args=[conn])
                thread.start()
