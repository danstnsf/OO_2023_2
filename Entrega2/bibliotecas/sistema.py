
class cart():
    def __init__(self):
        self.formas={}
    
    def inserirForma(self,forma):
        keys=list(self.formas.keys())
        list_tipos=[key.split('_')[0] for key in keys]
        forma.num=list_tipos.count(forma.tipo.replace('_',''))
        self.formas[forma.tipo+str(forma.num)]=forma
    
    def excluirForma(self,forma):
        del self.formas[forma.tipo + str(forma.num)]
    
    def listarFormas(self):
        for forma in self.formas.keys():
            print(forma)

    def info(self,forma):
        print(forma.info())
        