import base64

imagem = './img/porquinho-da-india-1536x1024.webp'

saida = './saidas/codificado3.txt'

with open(imagem, 'rb') as file_binary:
    data = file_binary.read()
    encoded = base64.b64encode(data)
    encoded_utf8 = encoded.decode('utf-8')
    print(encoded_utf8)

with open(saida, 'wt') as file:    
    file.write(encoded_utf8)