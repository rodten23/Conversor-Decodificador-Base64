import separar_nome_extensao
import base64

arquivo_a_converter = './originais/vida-simples-significativa-rotina.jpg'

nome_arquivo, extensao = separar_nome_extensao.arq_nome_ext(arquivo_a_converter)

saida_base64 = './saidas/' + nome_arquivo + extensao + '.base64' + '.txt'

with open(arquivo_a_converter, 'rb') as arquivo_binario:
    dados = arquivo_binario.read()
    codificado = base64.b64encode(dados)
    codificado_utf8 = codificado.decode('utf-8')

with open(saida_base64, 'wt') as base64_gerado:    
    base64_gerado.write(codificado_utf8)
