import socket
def fr(sock,lentgh):
    buffer = b''
    while len(buffer) < lentgh:
       buffer += sock.recv(lentgh - len(buffer))
    return buffer