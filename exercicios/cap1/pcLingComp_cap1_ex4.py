def alfabeto(texto):
    texto = texto.upper()
    letras = list()
    for letra in texto:
        if letra == ' ':
            continue
        else:
            letras.append(letra)
    letras_filtradas = set(letras)
    print(letras_filtradas)

alfabeto('O rato roeu a roupa do rei de Roma')
