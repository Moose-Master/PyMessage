import socket
import threading
import forcebytes
HOST = "68.168.164.146"  # The server's hostname or IP address
PORT = 65433  # The port used by the server
def send():
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
    name = input("Name? ")
    sending.start()
    receaving.start()
    receaving.join()