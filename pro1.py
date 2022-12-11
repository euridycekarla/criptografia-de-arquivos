import rsa, tarfile
from utils.hash import generateHash

while True:
  print("1 - Gerar conjunto de chaves")
  print("2 - Descompactar arquivos")
  print("3 - Comparar o Hash")

  option = int(input("Opção --> "))
  
  if (option == 1):
    publicKey, privateKey = rsa.newkeys(1024) #passo 1 - gerando chave pública e privada
    with open("public.pem", "wb") as file: # passo 2 - adicionando chave pública em um arquivo
      file.write(publicKey.save_pkcs1("PEM"))

    with open("private.pem", "wb") as file: # passo 2 - adicionando chave privada em um arquivo
      file.write(privateKey.save_pkcs1("PEM"))
  
  elif(option == 2):
    tarObj = tarfile.open("pacote.tar", "r")
    tarObj.extractall("pacote") # passo extra - descompactar os arquivos
    tarObj.close()

  elif (option == 3):
    textFileHash = generateHash("./pacote/arquivo.txt")

    with open("private.pem", "rb") as file:
      privateKey = rsa.PrivateKey.load_pkcs1(file.read())
  
    with open("./pacote/encryptedFileHash.txt", "rb") as file:
      fileHash = file.read()
      decryptFileHash = rsa.decrypt(fileHash, privateKey) # passo 7 - descriptografando o hash

    decryptFileHash = decryptFileHash.decode()
    if (textFileHash == decryptFileHash): # passo 8 - comparando hashs
      print("Arquivo autêntico")
    else:
      print("Arquivo não autêntico")
  else:
    break