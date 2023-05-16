import socket
def fr(sock,lentgh):
    buffer = b''
    while len(buffer) < lentgh:
       buffer += sock.recv(lentgh - len(buffer))
    return buffer
def sendmsg(sock):
   typ = "M"
   mesg = input()
   if mesg[0] == '^':
      typ = '^'
      mesg = mesg[1:]
   elif mesg[0] == '*':
      typ = '*'
      mesg = mesg[1:]   
   mesgts = str.encode(mesg,"utf-8")
   sock.sendall((len(mesg)).to_bytes(4,'big'))
   sock.sendall(str.encode(typ,'ascii'))
   sock.sendall(mesgts)