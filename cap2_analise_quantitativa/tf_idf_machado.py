from nltk.corpus import machado

#importar o corpus, limpá-lo e criar uma lista com apenas palavras limpas.
#função para limpeza de corpus.
def limpar(lista):
    lixo = '.,:;?!"`()[]{}\/|#$%^&*'
    quase_limpo = [x.strip(lixo).lower() for x in lista]

    return [x for x in quase_limpo if x.isalpha() or '-' in x]

obras = list()
for i in range(1, 10):
    obras.append('romance/marm0' + str(i) + '.txt')

#criar a lista apenas com palavras limpas.
colecao = list()
for obra in obras:
    stringona = machado.raw(obra)
    palavras = limpar(stringona.lower().split())
    colecao.append(palavras)


#importar o módulo math para operar logarítmo. Criar funções para calcular TF, DF, IDF e TF-IDF.
import math

def tf(termo, doc):
    return colecao[doc].count(termo) / len(colecao[doc])

def df(termo):
    return len([d for d in colecao if termo in d])

def idf(termo):
    return math.log10(len(colecao) / df(termo))

def tf_idf(termo, doc):
    return tf(termo, doc) * idf(termo)


#Fazer uma lista ordenando as palavras mais relevantes de um romance (Don Casumurro).
#Usa-se a função set() para não repetir as palavras. Por ser a iterável, seria ineficiente que houvesse milhares de palavras repetidas para iterar.
def mais_relevantes(doc):
    lista_total = [(tf_idf(p, doc), p) for p in set(colecao[doc])]

    return sorted(lista_total, reverse=True)[:50]

mr = mais_relevantes(7)
print(mr)

#Para retornar só as palavras, sem os valores, pode-se usar uma compreensão de lista:
#[p for v, p in mr]
