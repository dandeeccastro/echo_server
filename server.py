import socket

# Configurações iniciais
HOST = ''
PORT = 4200

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(1)
new_sock, address = sock.accept()

while True:
    message = new_sock.recv(1024)
    while not message:
        continue
    stringified_message = str(message,encoding='utf-8')
    if stringified_message == 'close':
        break
    else:
        print(stringified_message)

new_sock.close()
sock.close()
