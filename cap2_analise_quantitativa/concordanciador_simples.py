
def ler(nome_arq):
    arquivo = open(nome_arq, 'r', encoding = 'utf-8')
    conteudo_arq = arquivo.read()
    arquivo.close()

    return conteudo_arq

texto = ler(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\Ubirajara.txt')

def concordanciador(alvo, texto):
    texto = texto.replace('\n', ' ')
    texto = texto.replace('\t', ' ')

    ocorrencias = list()
    encontrado_aqui = texto.find(alvo, 0)
    while encontrado_aqui > 0:
        pos_inicial = encontrado_aqui - (40 - len(alvo) // 2)
        ocorrencias.append(texto[pos_inicial : pos_inicial + 80])

        encontrado_aqui = texto.find(alvo, encontrado_aqui + 1)

    return ocorrencias

resultados = concordanciador('serpente', texto)
for i in resultados:
    print(i)
