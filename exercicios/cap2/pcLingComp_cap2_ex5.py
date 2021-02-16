import corpus
import nltk
from nltk.corpus import machado
import matplotlib.pyplot as plt
vazias = nltk.corpus.stopwords.words('portuguese')

#abrir "Memórias Póstumas de Brás Cubas".
texto = machado.raw('romance/marm05.txt')

# 1. Conte o número de caracteres do texto (sem limpar).
print('Número de caracteres (sem limpar):', len(texto))


#---


#2. Limpe o corpus.
# !!! tem que primeiro usar split(), criar uma lista de palavras (sujas), e daí fazer a limpeza.
# se fizer a limpeza direto, vai retornar uma lista de letras, e vai ser impossível trabalhar com palavras.
palavras_sujas = texto.split()
palavras = corpus.limpar(palavras_sujas)


#---


#3. Conte as palavras do texto.
print('Número de palavras (absoluto):', len(palavras))


#---


#4. Calcule a riqueza lexical do texto.
vocabulario = set(palavras)
riqueza_lexical = len(vocabulario) / len(palavras)
print('Riqueza lexical:', riqueza_lexical)


#---


#5. Divida as palavras do texto em função de seu número de ocorrências e responda:
#  As vinte palavras mais frequentes de Memórias Póstumas são semelhantes às palavras mais frequentes de Ubirajara?
#  O que isso representa em termos linguístico-discursivos, isto é, quanto ao seu uso concreto da língua?

#print('Memórias Póstumas de Brás Cubas:', '\n')
#dic = corpus.ocorrencias(palavras)
#mf = sorted(dic.items(), key=lambda tupla:tupla[1], reverse=True) [:20]
#for palavra, n in mf:
#    print(palavra, '\t', n)
#print('\n')

#print('Ubirajara', '\n')
#ubirajara = corpus.ler(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\Ubirajara.txt')
#palavras_sujas = ubirajara.split()
#palavras = corpus.limpar(palavras_sujas)
#dic = corpus.ocorrencias(palavras)
#mf = sorted(dic.items(), key=lambda tupla:tupla[1], reverse=True) [:20]
#for palavra, n in mf:
#    print(palavra, '\t', n)
#print('\n')

#Resposta: as vinte palavras são semelhantes, mas com algumas diferenças. Em "Ubirajara", aparece a palavra "guerreiro", já que esta
#é uma palavra-chave dentro dessa obra.
#Responsta: em termos linguístico-discursivo, dificilmente se poderia extrair uma conclusão apenas com esses dados, já que a maioria
#das palavras são funcionais ou vazias de significado. Ainda assim, percebe-se que em Memórias Póstumas, aparece o verbo "é" (que não
#aparece em Ubirajara), indicando que Machado fazia uso maior de verbos de ligação.


#---


#6. Retire da lista de palavras frequentes as palavras vazias. Compare novamente os resultados entre os dois textos.

#print('Palavras plenas de Memórias Póstumas de Brás Cubas:', '\n')
#palavras_plenas = [x for x in palavras if x not in vazias]
#dic = corpus.ocorrencias(palavras_plenas)
#mf = sorted(dic.items(), key=lambda tupla:tupla[1], reverse=True) [:20]
#for palavra, n in mf:
#    print(palavra, '\t', n)
#print('\n')

#print('Palavras plenas de Ubirajara', '\n')
#ubirajara = corpus.ler(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\Ubirajara.txt')
#palavras_sujas = ubirajara.split()
#palavras = corpus.limpar(palavras_sujas)
#palavras_plenas = [x for x in palavras if x not in vazias]
#dic = corpus.ocorrencias(palavras_plenas)
#mf = sorted(dic.items(), key=lambda tupla:tupla[1], reverse=True) [:20]
#for palavra, n in mf:
#    print(palavra, '\t', n)
#print('\n')

#Resposta: em Ubirajara, aparecem palavras típicos para uma obra indianista, fazendo alusão à nação, guerra e
#lugares-comuns épicos de grandiosidade, como "nação", "guerreiro", "chefe", "grande". Em Memórias Póstumas, aparecem
#palavras como "virgília", "olho", "nada", "vida", "tempo", "casa".


#---


#7. Crie uma lista com os hápax legomena do texto de Machado de Assis e reponda:
#  Comparando a extensão dessa lista com aquele dos hápax legomena de Ubirajara, o que se pode inferir?
#  Quais são os hápax legomena em comum nos dois textos?

print('Hápax de Memórias Póstumas de Brás Cubas:', '\n')
hapax_bc = [x for x in palavras if palavras.count(x) == 1]
print(len(hapax_bc))
print('\n')

print('Hápax de Ubirajara', '\n')
ubirajara = corpus.ler(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\Ubirajara.txt')
palavras_sujas = ubirajara.split()
palavras = corpus.limpar(palavras_sujas)
hapax_ub = [x for x in palavras if palavras.count(x) == 1]
print(len(hapax_ub))
print('\n')

conj_bc = set(hapax_bc)
conj_ub = set(hapax_ub)
hapax_comum = conj_bc & conj_ub
print(hapax_comum)

#Resposta:
#Hápax de Memórias Póstumas de Brás Cubas: 6259
#Hápax de Ubirajara: 4361
#
