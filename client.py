import socket
import random
from random import randint
from threading import Timer
from time import sleep

sock = socket.socket()
sock.connect(('localhost', 1489))
answer = "success"
lost = "lost"
while True:
    data = sock.recv(1024)
    tmp = randint(1,4)
    if tmp == 2:
        print("received command", data.decode())
        sock.send(answer.encode())
        if data.decode() == "quit":
            sock.close()
    else:
        sock.send(lost.encode())
        print("lost")