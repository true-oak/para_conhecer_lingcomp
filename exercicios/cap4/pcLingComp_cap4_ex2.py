## Exercício 2. Implemente novamente esse classificador de mensagens utilizando a fórmula
# baseada em logaritmos apresentada neste capítulo.
# obs. eu assumi que a base do logaritmo é 10, pq no livro está omitida.
# obs. eu assumi que era para desconsiderar a mudança feita no exercício 1 e usar a implementação original.
# a mudança feita no exercício 1 parecia não funcionar com logaritmos, pois o resultado dava errado.

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
def p_em_spam(palavra):
    return (em_spam[palavra] + k) / (spams + 2 * k)
def p_em_nao_spam(palavra):
    return (em_nao_spam[palavra] + k) / (nao_spams + 2 * k)


## CLASSIFICAÇÃO DAS MENSAGENS
# para o exercício, coloquei math.log10() em tudo.
def classificar(mensagem):
    score_spam = math.log10(p_spam)
    score_nao_spam = math.log10(p_nao_spam)

    for palavra in vocab:
        if palavra in atributos(mensagem):
            score_spam += math.log10(p_em_spam(palavra))
            score_nao_spam += math.log10(p_em_nao_spam(palavra))
        else:
            score_spam += 1 - math.log10(p_em_spam(palavra))
            score_nao_spam += 1 - math.log10(p_em_nao_spam(palavra))

    if score_spam > score_nao_spam:
        return 'spam'
    else:
        return 'não spam'



spams = 0
nao_spams = 0
em_spam = defaultdict(int)
em_nao_spam = defaultdict(int)
vocab = set()


## PREPARAÇÃO DOS DADOS E CONTAGEM DE ATRIBUTOS
# para cada linha no corpus de treino, transforma a linha numa string com str()
corpus_treino = open(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\cap4_naive_bayes\corpus_treino.txt', 'r', encoding='utf-8')

for dado in corpus_treino:
    classe = dado[0]    # extrai a classificação (elemento [0] da linha, 0 ou 1)
    texto = dado[2:]    # extrai a mensagem (elemento do terceiro caractere em diante)
    palavras = atributos(texto)

    vocab |= palavras

# atualiza o valor das variáveis
    if classe == '1':
        spams += 1
        for x in palavras:
            em_spam[x] += 1
    elif classe == '0':
        nao_spams += 1
        for x in palavras:
            em_nao_spam[x] += 1
corpus_treino.close()


## SUAVIZAÇÃO DO CLASSIFICADOR
# k = 1. o número total de spams e não-spams aumenta em 2k. O tamanho do corpus inteiro aumenta em 4k.
k = 1
p_spam = (spams + 2 * k) / (spams + nao_spams + 4 * k)
p_nao_spam = (nao_spams + 2 * k) / (spams + nao_spams + 4 * k)
