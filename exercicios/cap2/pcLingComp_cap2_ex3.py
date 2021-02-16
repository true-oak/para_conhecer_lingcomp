import corpus
import matplotlib.pyplot as plt

while True:
    dir = input('Digite o diretório: ')
    nome_obra = input('Qual o nome da obra? ')

#ler o texto. limpar o texto. ordenar as letras mais frequentes.
    texto = corpus.ler(dir)
    string_limpo = corpus.limpar(texto)
    dicio = corpus.ocorrencias(string_limpo)
    mf = sorted(dicio.items(), key=lambda tupla:tupla[1], reverse=True)
    for letra, n in mf:
        print(letra, '\t', n)

#criar um gráfico das letras mais frequentes.
    letras = [key for (key, value) in mf]
    y = [value for (key, value) in mf]
    plt.bar(letras, y)
    plt.ylabel('Ocorrência da letra')
    plt.title('Ocorrência de letras em' + ' ' + nome_obra)
    plt.show()

    continue
