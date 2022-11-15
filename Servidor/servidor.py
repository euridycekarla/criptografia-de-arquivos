import socket 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',8080))
server.listen(2)

connection, adress = server.accept()
nomeArquivo= connection.recv(1024).decode()

with open(nomeArquivo, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print('Uhull, o arquivo foi enviado!')