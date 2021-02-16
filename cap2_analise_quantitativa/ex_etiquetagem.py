import spacy
nlp = spacy.load('pt_core_news_lg')
doc = nlp('Será que vai funcionar essa etiquetagem?')
etiq = [(x.orth_, x.pos_) for x in doc]
print(etiq)
