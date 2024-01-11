import base64

saida = './saidas/imagem_decodificada3.webp'

arquivo_base64 = './saidas/codificado3.txt'

with open(arquivo_base64, 'rt') as file_codicado:
    data = file_codicado.read()

encoded = data.encode('utf-8')

with open(saida, 'wb') as file:
    saida_decodificada = base64.decodebytes(encoded)
    file.write(saida_decodificada)
    