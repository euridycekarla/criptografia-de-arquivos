import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost',8080))
print('Eba! Estás conectado com o servidor.\n')

nomeArquivo = str(input('Qual arquivo deseja receber do servidor?'))

client.send(nomeArquivo.encode())
with open(nomeArquivo, 'wb') as file:
    while 1 :
      data = client.recv(100000)
      if not data:
        break 
      file.write(data)
print(f'{nomeArquivo} recebido!')