import socket
import threading
import DefOther
msgtyp = 'M'
HOST = "68.168.164.146"  # The server's hostname or IP address
PORT = 65433  # The port used by the server
def send():
    s.sendall((len(name)).to_bytes(4,'big'))
    s.sendall(str.encode("^",'ascii'))
    s.sendall(str.encode(name,'ascii'))
    while True:
        DefOther.sendmsg(s)
sending = threading.Thread(target=send)
def get():
        try:
            while True:
                bytelen = int.from_bytes(DefOther.fr(s,4),byteorder="big")
                msgtyp = DefOther.fr(s,1).decode('ascii')
                data = (DefOther.fr(s,bytelen)).decode('utf-8')
                if msgtyp == "M":
                    print(data)
                elif msgtyp == '^':
                    exit(0)
        except Exception:
            print('The server is now offline')
            print('Please try again soon')
            exit(0)
receaving = threading.Thread(target=get)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    name = input("Name? ")
    sending.start()
    receaving.start()
    receaving.join()