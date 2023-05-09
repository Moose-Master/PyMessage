from socket import *
import threading 
HOST = "68.168.164.146"  # The server's hostname or IP address
PORT = 65433  # The port used by the server

def send():
    while True:
        print("Ready")
        s.sendall(str.encode(input()))
sending = threading.Thread(target=send)
def get():
        while True:
            data = s.recv(1024)
            print(data)
receaving = threading.Thread(target=get)
with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    sending.start()
    receaving.start()
    receaving.join()
    