import os
import base64

imagem = './img/porquinho-da-india-1536x1024.webp'

def separar_nome_extensao(caminho_completo):
    global nome_arquivo
    caminho_sem_extensao = os.path.splitext(caminho_completo)[0]
    nome_arquivo = caminho_sem_extensao.split('/')[-1]
    return nome_arquivo
    
separar_nome_extensao(imagem)

saida = './saidas/' + nome_arquivo + '.txt'

with open(imagem, 'rb') as file_binary:
    data = file_binary.read()
    encoded = base64.b64encode(data)
    encoded_utf8 = encoded.decode('utf-8')
    print(encoded_utf8)

with open(saida, 'wt') as file:    
    file.write(encoded_utf8)