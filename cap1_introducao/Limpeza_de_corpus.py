def ler(nome_arq):
    arquivo = open(nome_arq, 'r', encoding = 'utf-8')
    conteudo_arq = arquivo.read()
    arquivo.close()

    return conteudo_arq

texto = ler(r'C:\Users\tkrhy\Documents\Python\Para_Conhecer_LingComp\Ubirajara.txt')
palavras = texto.split()

def limpar(lista):
    lixo = '.,:;?!"`()[]{}\/|#$%^&*'
    quase_limpo = [x.strip(lixo).lower() for x in lista]

    return [x for x in quase_limpo if x.isalpha() or '-' in x]

print(len(palavras))
print(len(limpar(palavras)))
