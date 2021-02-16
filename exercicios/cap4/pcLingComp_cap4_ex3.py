## Exercício 3. classificar resultados submetidos a uma conferência de linguística, a partir das palavras-chave, em duas classes:
# linguística teórica (0) ou linguística aplicada (1).
# obs. o corpus de treino é o 'corpus_treino_ex3.txt'.

import math
import corpus
from collections import defaultdict


## EXTRAÇÃO DE ATRIBUTOS
# quebra a mensagem numa lista de palavras. limpa as palavras. retorna um conjunto para eliminar repetições.
def atributos(mensagem):
    palavras = mensagem.split()
    palavras = corpus.limpar(palavras)

    return set(palavras)


## PROBABILIDADES SUAVIZADAS
def p_em_lt(palavra):
    return (em_lt[palavra] + k) / (lts + 2 * k)
def p_em_la(palavra):
    return (em_la[palavra] + k) / (la + 2 * k)


## CLASSIFICAÇÃO DAS MENSAGENS
def classificar(mensagem):
    score_lt = math.log10(p_lt)
    score_la = math.log10(p_la)

    for palavra in vocab:
        if palavra in atributos(mensagem):
            score_lt += math.log10(p_em_lt(palavra))
            score_la += math.log10(p_em_la(palavra))
        else:
            score_lt += 1 - math.log10(p_em_lt(palavra))
            score_la += 1 - math.log10(p_em_la(palavra))

    if score_lt > score_la:
        return 'lt'
    else:
        return 'la'



lt = 0
la = 0
em_lt = defaultdict(int)
em_la = defaultdict(int)
vocab = set()


## PREPARAÇÃO DOS DADOS E CONTAGEM DE ATRIBUTOS
# para cada linha no corpus de treino, transforma a linha numa string com str()
corpus_treino = open(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\exercicios\cap4\corpus_treino_ex3.txt', 'r', encoding='utf-8')

for dado in corpus_treino:
    classe = dado[0]    # extrai a classificação (elemento [0] da linha, 0 ou 1)
    texto = dado[2:]    # extrai a mensagem (elemento do terceiro caractere em diante)
    palavras = atributos(texto)

    vocab |= palavras

# atualiza o valor das variáveis
    if classe == '0':
        lt += 1
        for x in palavras:
            em_lt[x] += 1
    elif classe == '1':
        la += 1
        for x in palavras:
            em_la[x] += 1
corpus_treino.close()


## SUAVIZAÇÃO DO CLASSIFICADOR
# k = 1. o número total de lts e não-lts aumenta em 2k. O tamanho do corpus inteiro aumenta em 4k.
k = 1
p_lt = (lt + 2 * k) / (lt + la + 4 * k)
p_la = (la + 2 * k) / (lt + la + 4 * k)
