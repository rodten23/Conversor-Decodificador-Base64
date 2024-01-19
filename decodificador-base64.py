import separar_nome_extensao
import base64

txt_base64 = './saidas/vida-simples-significativa-rotina.jpg.base64.txt'

nome_base64, extensao_original = separar_nome_extensao.base64_nome_ext(txt_base64)

saida_descodificada = './saidas/' + nome_base64 + '.' + extensao_original

with open(txt_base64, 'rt') as txt_descodificar:
    dados = txt_descodificar.read()
    codigo_base64 = dados.encode('utf-8')

with open(saida_descodificada, 'wb') as arquivo_recriado:
    binario_recriado = base64.decodebytes(codigo_base64)
    arquivo_recriado.write(binario_recriado)
    