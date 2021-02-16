from collections import defaultdict
import nltk
vazias = nltk.corpus.stopwords.words('portuguese')

#função para abrir um texto e retornar os seus conteúdos.
def ler(nome_arq):
    arquivo = open(nome_arq, 'r', encoding = 'utf-8')
    conteudo_arq = arquivo.read()
    arquivo.close()

    return conteudo_arq

#função para limpar um texto.
def limpar(lista):
    lixo = '.,:;?!"`()[]{}\/|#$%^&*'
    quase_limpo = [x.strip(lixo).lower() for x in lista]

    return [x for x in quase_limpo if x.isalpha() or '-' in x]



texto = ler(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\Ubirajara.txt')
palavras_sujas = texto.split()
palavras = limpar(palavras_sujas)

hapax = [x for x in palavras if palavras.count(x) == 1]
print(len(hapax))

stemmer = nltk.stem.RSLPStemmer()
raizes = [stemmer.stem(x) for x in set(palavras)]
hapax = [x for x in raizes if raizes.count(x) == 1]
print(len(hapax))
