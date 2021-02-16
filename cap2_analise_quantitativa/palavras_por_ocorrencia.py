from collections import defaultdict
import nltk
vazias = nltk.corpus.stopwords.words('portuguese')

def ler(nome_arq):
    arquivo = open(nome_arq, 'r', encoding = 'utf-8')
    conteudo_arq = arquivo.read()
    arquivo.close()

    return conteudo_arq

def limpar(lista):
    lixo = '.,:;?!"`()[]{}\/|#$%^&*'
    quase_limpo = [x.strip(lixo).lower() for x in lista]

    return [x for x in quase_limpo if x.isalpha() or '-' in x]

def ocorrencias(lista_palavras):
    dicionario = defaultdict(int)
    for p in lista_palavras:
        dicionario[p] += 1
    return dicionario

texto = ler('Ubirajara.txt')
palavras = texto.split()
palavras_limpas = limpar(palavras)

dic = ocorrencias(palavras_limpas)
mf = sorted(dic.items(), key=lambda tupla:tupla[1], reverse=True) [:20]
for palavra, n in mf:
    print(palavra, '\t', n)

frequentes_plenas = [x for x in mf if x[0].lower() not in vazias]
print(frequentes_plenas)
