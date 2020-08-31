import socket 

HOST = 'localhost'
PORT = 4200

sock = socket.socket()
sock.connect((HOST,PORT))

while True:
    user_message = input() 
    sock.send( bytes(user_message,encoding='utf-8') )
    if user_message == 'close':
        break

sock.close()
