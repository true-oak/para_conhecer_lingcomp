import re
from collections import defaultdict
import corpus


## EXTRATOR DE N-GRAMAS
def ngramas(n, sent):
    return [tuple(sent[i:i + n]) for i in range(len(sent) - n + 1)]

## PROBABILIDADES
# Com suavização de Laplace
def prob_uni(x):
    C = sum(unigramas.values())
    V = len(novo_vocab)
    return (unigramas[x] + 1) / (C + V)

def prob_bi(x):
    V = len(novo_vocab)
    return (bigramas[x] + 1) / (unigramas[(x[0],)] + V)

## PREVISÃO
# prevê a próxima palavra
def prever(palavra):
    lista = [ch for ch in bigramas.keys() if ch[0] == palavra]
    ordem = sorted(lista, key=lambda x:prob_bi(x), reverse=True)
    topo = ordem[0][1]
    return topo


## LEITURA E PREPARAÇÃO DO CORPUS
corpus_base = corpus.ler('corpus_bruto.txt')
## transformar o corpus em uma lista de sentenças
# substituir os delimitadores de sentença (por simplicidade, aqui definiddos como pontuações) por um caractere único '#'.
corpus_pontuacao = re.sub(r'\.|\!|\?', '#', corpus_base)
# usar split('#') para dividir as sentenças, com '#'  como delimitador da divisão.
sents = corpus_pontuacao.split('#')
##criar uma lista de sublistas, cada uma correspondendo a uma sentença.
#as senteças têm marcador de início e fim, além de serem limpas.
#usa o mesmo nome de variável 'sent' para substituir a outra e poupar memória.
sents = [['<s>'] + corpus.limpar(x.split()) + ['</s>'] for x in sents]



##GRAVAÇÃO DO CORPUS PREPARADO
#gravar o arquivo com a função open(). o modo é 'w', significando 'writing'
c_p = open('corpus_preparado.txt', 'w', encoding='utf-8')
#transformar objeto iterável (lista, nesse caso) em string com join(). separar strings com ' '.
for sentenca in sents:
    str = ' '.join(sentenca)
    c_p.write(str + '\n')
c_p.close()


## dividir o corpus preparado em corpus de treinamento e de teste. 80% para treno e 20% para teste.
# readlines() lê uma linha de texto a cada vez e gera uma lista de linhas, muito conveniente.
corpus_tt = open('corpus_preparado.txt', 'r', encoding='utf-8')
c_tt = corpus_tt.readlines()
corpus_tt.close()

# dividir a lista de linhas em corpora de treinamento e teste.
corte = int(len(c_tt) * 0.8) # 80% do tamanho
treino = c_tt[:corte] # 0 -> corte-1 (80%)
teste = c_tt[corte:]  # corte -> última sentença (20%)


## GRAVAÇÃO CORPUS DE TREINAMENTO
tr = open('corpus_treino.txt', 'w', encoding='utf-8')
for sent in treino:
    tr.write(sent)
tr.close()


## GRAVAÇÃO CORPUS DE TESTE
ts = open('corpus_teste.txt', 'w', encoding='utf-8')
for sent in teste:
    ts.write(sent)
ts.close()


## construção do modelo
corpus_treino = open('corpus_treino.txt', 'r', encoding='utf-8')
c_t = corpus_treino.readlines()
corpus_treino.close()

# extrair vocabulário e contar ocorrência de seus itens.
vocab = set()
contagem = defaultdict(int)
for linha in c_t:
    sent = linha.split()
    for palavra in sent:
        vocab |= {palavra}
        contagem[palavra] += 1

# filtrar hapax legomena e substitui-los por '<DES>', palavras desconhecidas.
hapax = [palavra for palavra in contagem.keys() if contagem[palavra] == 1]
hapax = set(hapax)
novo_vocab = vocab - hapax
novo_vocab |= {'<DES>'}


## CRIAR DICIONÁRIOS DE UNIGRAMAS E BIGRAMAS
unigramas = defaultdict(int)
bigramas = defaultdict(int)

for linha in c_t:
    sent = linha.split()

    for i in range(len(sent)):
        if sent[i] in hapax:
            sent[i] = '<DES>'   # substituir hapax por '<DES>'

    for x in ngramas(1, sent):
        unigramas[x] += 1

    for x in ngramas(2, sent):
        bigramas[x] += 1



print(prever('o'))
