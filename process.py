# Bibliotecas Necessárias
import spacy
import en_core_web_sm
import pt_core_news_sm

class Process(object):
    def __init__(self, arquivo):
        self.arq = arquivo
        self.list_org = list()

    # Função para carregar o arquivo    
    def load_arquivo(self):
        with open(self.arq, 'r', encoding='utf-8') as file:
            self.texto = file.read()
        return self.texto

    # Função para iniciar o [spacy]
    def init_spacy(self):
        self.nlp = spacy.load('pt_core_news_sm')
        self.doc = self.nlp(self.texto)
        return self.doc.ents

    # Função para identificar as entidades por label, nesse caso [ORG]
    def identify_entites(self):
        for self.entidades in self.doc.ents:
            if self.entidades.label_ == 'ORG':
                self.list_org.append(self.entidades.text)
        print(f'Listas de Organizações: {self.list_org}')

    # Função para inicializar todas funções
    def main(self):
        obj.load_arquivo()
        obj.init_spacy()
        obj.identify_entites()
        
# Instanciando o Objeto e a função [main]        
if __name__ == '__main__':
    obj = Process('arquivo.txt') # arquivo.txt salvo no dir raiz
    obj.main()