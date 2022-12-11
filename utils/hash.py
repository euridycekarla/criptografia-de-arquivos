import hashlib

def generateHash(arquivoNome):
  hashMd5 = hashlib.md5()

  with open(arquivoNome, "rb") as file:
    fileLoading = 0
    while(fileLoading != b''):
      fileLoading = file.read(1024)
      hashMd5.update(fileLoading)

  hashFile = hashMd5.hexdigest()

  return hashFile