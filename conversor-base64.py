import os
import base64

imagem = './img/porquinho-da-india-1536x1024.webp'

def separar_nome_extensao(caminho_completo):
    caminho, extensao = os.path.splitext(caminho_completo)
    nome_arquivo = caminho.split('/')[-1]
    print(caminho, '===', nome_arquivo, '===', extensao)

separar_nome_extensao(imagem)

saida = './saidas/codificado3.txt'

with open(imagem, 'rb') as file_binary:
    data = file_binary.read()
    encoded = base64.b64encode(data)
    encoded_utf8 = encoded.decode('utf-8')
    print(encoded_utf8)

with open(saida, 'wt') as file:    
    file.write(encoded_utf8)