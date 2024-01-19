import os

def arq_nome_ext(caminho_completo):
    global nome_arquivo, extensao
    caminho_sem_extensao, extensao = os.path.splitext(caminho_completo)
    nome_arquivo = caminho_sem_extensao.split('/')[-1]
    return nome_arquivo, extensao

def base64_nome_ext(caminho_completo):
    global nome_base64, extensao_original
    arquivo_base64 = caminho_completo.split('/')[-1]
    nome_base64, extensao_original = arquivo_base64.split('.')[0:2]
    return nome_base64, extensao_original

if(__name__ == '__main__'):
    arq_nome_ext()
    base64_nome_ext()
