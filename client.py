import socket
import threading
import DefOther
msgtyp = 'M'
HOST = "68.168.164.146"  # The server's hostname or IP address
PORT = 21894  # The port used by the server
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
                    print("That name is already in use")
                    print("Please try again")
                elif msgtyp =='&':
                    print("You have been kicked")
                    exit(0)
        except Exception:
            print('The server is now offline')
            print('Please try again soon')
            exit(0)
receaving = threading.Thread(target=get)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    help = input("Do you want some quick info on PyMsg? y/n? ")
    if help == "y":
        print("""
Hello and Welcome to PyMsg")
This was made almost completly by Ivan with some help from Magnus
Use ^name to change your username
(replace name with what you want your name to be)
Use @name@msg to privately message another user
You can do a group privet message with @Name@Name@Message
You can have as many users in a private group message as you want
(replace name with the user you want to message and msg with the message you want to send)""")
    name = input("Name? ")
    sending.start()
    receaving.start()
    receaving.join()