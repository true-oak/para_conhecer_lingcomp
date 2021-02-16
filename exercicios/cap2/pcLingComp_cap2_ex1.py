import corpus

string = 'Esta é uma string para testar a solução.'
string_limpo = corpus.limpar(string)
dicio = corpus.ocorrencias(string_limpo)
mf = sorted(dicio.items(), key=lambda tupla:tupla[1], reverse=True) [:20]
for letra, n in mf:
    print(letra, '\t', n)
