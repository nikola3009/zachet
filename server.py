import socket
from threading import Timer
from time import sleep

sock = socket.socket()
sock.bind(('', 1489))
sock.listen(1)
flag = 0
conn, addr = sock.accept()
print("connected ")
while True:
    print("enter command")
    data=input()
    conn.send(data.encode())
    answer = conn.recv(512)
    while answer.decode() != "success":
        conn.send(data.encode())
        answer = conn.recv(512)
        sleep(60)
        print("lost")

            
    