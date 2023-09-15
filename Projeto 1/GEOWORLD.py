import numpy as np
class Forma:
    contador=0
    
    def __init__(self,coordx,coordy):
       self.coordx=coordx
       self.coordy=coordy
       self.npontos=len(self.coordx)       
       Forma.contador+=1

    def area(self):
        if self.npontos in [1,2]: return None
        

    @staticmethod
    def tri_area(xl,yl):
        trimatrix=np.array([(1,1,1),tuple(xl),tuple(yl)])
        return np.abs(0.5*np.linalg.det(trimatrix))

    @staticmethod
    def circ_area(raio):
        return np.pi*raio^2



f1=Forma([[0,0,2,2],[0,2,2,0]])
print(f1.area())

