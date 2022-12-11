import rsa, tarfile, hashlib
from utils.hash import generateHash

with open("public.pem", "rb") as file:
  publicKey = rsa.PublicKey.load_pkcs1(file.read())

print("passo 3 - gerando o hash de um arquivo")
hash = generateHash("arquivo.txt") # passo 3 - gerando o hash de um arquivo

print("passo 4 - criptografando código hash")
encryptedFileHash = rsa.encrypt(hash.encode(), publicKey) # passo 4 - criptografando código hash

print("adicionando hash criptografado a um arquivo")
with open("encryptedFileHash.txt", "wb") as file: # adicionando hash criptografado a um arquivo
  file.write(encryptedFileHash)

tarObj = tarfile.open("pacote.tar", "w") # passo 5 - criando pacote compactado
tarObj.add("arquivo.txt") # adicionando arquivo no pacote
tarObj.add("encryptedFileHash.txt") # adicionando arquivo no pacote
tarObj.close() # fechando pacote