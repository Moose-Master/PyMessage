import socket
import threading
import forcebytes
HOST = "68.168.164.146"  # The server's hostname or IP address
PORT = 65433  # The port used by the server
names = []
def send():
    name = input("Name? ")
    for i in range(len(names)):
        if names[i] == name:
             print("That name is taken")
             exit()
        else:
             print("👍")    
    s.sendall(str.encode(name))
    while True:
        print("Ready")
        mesg = str.encode(name +": " + input(),"utf-8")
        s.sendall((len(mesg)).to_bytes(4,'big'))
        s.sendall(mesg)
sending = threading.Thread(target=send)
def get():
        while True:
            bytelen = int.from_bytes(forcebytes.fr(s,4),byteorder="big")
            data = (forcebytes.fr(s,bytelen)).decode('utf-8')
            print(data)
receaving = threading.Thread(target=get)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #nameslen = int(s.recv(1024))
    nameslen = int.from_bytes(forcebytes.fr(s,4), byteorder='big')
    for i in range(nameslen):
        namelen = int.from_bytes(forcebytes.fr(s,4), byteorder='big')
        names.append((forcebytes.fr(s,namelen)).decode('utf-8'))
    sending.start()
    receaving.start()
    receaving.join()