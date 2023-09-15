import numpy as np

class Ponto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def coord(self):
        return [self.x,self.y]

class Linha:
    def __init__(self,x,y):
        self.p1=Ponto(x[0],y[0])
        self.p2=Ponto(x[1],y[1])
        self.comp=np.sqrt((self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2)
    def coord(self):
        return [self.p1.coord(),self.p2.coord()]

class Circulo:
    def __init__(self,xc,yc,raio):
        self.centro=Ponto(xc,yc)
        self.raio=raio
        self.area=np.pi*raio**2
        self.perimetro=2*np.pi*raio

class Poligono:
    def __init__(self,x,y):
        self.npontos=len(x)
        self.vertices=[Ponto(x[i],y[i]) for i in range(0,self.npontos)]
        self.linhas=[Linha([self.vertices[i].x,self.vertices[i+1].x],[self.vertices[i].y,self.vertices[i+1].y]) for i in range(0,self.npontos-1)]+[Linha([self.vertices[self.npontos-1].x,self.vertices[0].x],[self.vertices[self.npontos-1].y,self.vertices[0].y])]

def Triangulo(Poligono):
    pass

