import socket
def fr(sock,lentgh):
    buffer = b''
    while len(buffer) < lentgh:
       buffer += sock.recv(lentgh - len(buffer))
    return buffer
def sendmsg(type,sock):
   mesg = str.encode(input(),"utf-8")
   sock.sendall((len(mesg)).to_bytes(4,'big'))
   sock.sendall(str.encode("M",'ascii'))
   sock.sendall(mesg)