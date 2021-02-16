from nltk.corpus import machado
import spacy
nlp = spacy.load('pt_core_news_lg')
import statistics as stat

#criar a lista de obras
obras = list()
for i in range(1, 6):
    obras.append('romance/marm0' + str(i) + '.txt')

for i in range(1, 6):
    obras.append('cronica/macr0' + str(i) + '.txt')

#etiquetar as palavras, extrair os advérbios, e contar a porcentagem de advérbios.
cont_adv = list()
for obra in obras:
    print(obra)
    s = machado.raw(obra)
    doc = nlp(s)
    etiq = [(pal.orth_, pal.pos_) for pal in doc]
    adv = [(ort, pos) for (ort, pos) in etiq if pos == 'ADV']
    cont_adv.append(len(adv) / len(etiq))

#calcular as médias e desvios-padrões para romances e crônicas.
rom_m = stat.mean(cont_adv[:4])
rom_dp = stat.stdev(cont_adv[:4])
cro_m = stat.mean(cont_adv[5:])
cro_dp = stat.stdev(cont_adv[5:])


#gráfico de barras
import matplotlib.pyplot as plt

tipo_obra = ('Romances', 'Crônicas')
x = [0, 1]
y = [rom_m, cro_m]
dp = [rom_dp, cro_dp]
plt.bar(x, y, yerr = dp)
plt.xticks(x, tipo_obra)
plt.ylabel('Percentual médio de advérbios (%)')
plt.title('Adverbiação média em obras de M. de Assis')

plt.show()


#gráfico de pizza
from collections import defaultdict

lixo = ['PUNCT', 'SPACE', 'X', 'SYM', 'NUM', 'INTJ']
pos2 = [pos for (pal, pos) in etiq if pos not in lixo]

cont = defaultdict(int)
for p in pos2:
    cont[p] += 1

nomes = cont.keys()
ocorrencias = cont.values()

plt.pie(ocorrencias, labels = nomes, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
