import os

def arq_ext(caminho_completo):
    global nome_arquivo, extensao
    caminho_sem_extensao, extensao = os.path.splitext(caminho_completo)
    nome_arquivo = caminho_sem_extensao.split('/')[-1]
    return nome_arquivo, extensao

if(__name__ == '__main__'):
    arq_ext()
