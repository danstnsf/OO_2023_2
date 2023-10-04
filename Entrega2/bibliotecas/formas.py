import numpy as np

class Ponto:
    def __init__(self,x,y):
        self.tipo='Ponto_'
        self.x=x
        self.y=y
        self.num=0
    def coord(self):
        return [self.x,self.y]
    
    def info(self):
        return {'A coordenada do ponto é ': self.coord()}
    
class Linha:
    def __init__(self,x,y):
        self.tipo='Linha_'
        self.p1=Ponto(x[0],y[0])
        self.p2=Ponto(x[1],y[1])
        self.comp=np.sqrt((self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2)
        self.num=0
    def coord(self):
        return [self.p1.coord(),self.p2.coord()]

    def info(self):
        return {'A linha é definida pelos pontos ':self.coord()}

class Circulo:
    def __init__(self,xc,yc,raio):
        self.tipo='Circulo_'
        self.centro=Ponto(xc,yc)
        self.raio=raio
        self.area=np.pi*raio**2
        self.perimetro=2*np.pi*raio
        self.num=0
    
    def info(self):
        return{'Centro em ':self.centro.coord(),'Raio ':self.raio,'Area ':self.area,'Perimetro ':self.perimetro}

class Poligono:
    def __init__(self,x,y):
        
        self.npontos=len(x)
        self.vertices=[Ponto(x[i],y[i]) for i in range(0,self.npontos)]
        self.linhas=[Linha([self.vertices[i].x,self.vertices[i+1].x],[self.vertices[i].y,self.vertices[i+1].y]) for i in range(0,self.npontos-1)]+[Linha([self.vertices[self.npontos-1].x,self.vertices[0].x],[self.vertices[self.npontos-1].y,self.vertices[0].y])]
        self.centroide=Ponto(sum(x)/self.npontos,sum(y)/self.npontos)
        self.area=0
        for i in range(self.npontos):
            x1,y1=self.vertices[i].coord()
            x2,y2=self.vertices[(i+1)%self.npontos].coord()
            self.area+=(x1*y2-x2*y1)
        self.area=abs(self.area)/2.0

        self.perimetro=0
        for i in range(self.npontos):
            self.perimetro+=self.linhas[i].comp
        

    def rotacionar(self,th):
        a=th*np.pi/180
        P=np.array([[self.vertices[i].x for i in range(self.npontos)],[self.vertices[i].y for i in range(self.npontos)]],dtype=float)
        P[0,:]=[x-self.centroide.x for x in P[0,:]]
        P[1,:]=[y-self.centroide.y for y in P[1,:]]
        M=np.array([[np.cos(a),np.sin(a)],[-np.sin(a),np.cos(a)]],dtype=float)
        P=np.dot(M,P)
        P[0,:]=[x+self.centroide.x for x in P[0,:]]
        P[1,:]=[y+self.centroide.y for y in P[1,:]]
        return Poligono(P[0,:],P[1,:])

def Triangulo(Poligono):
    def __init__(self,x,y):
        super().__init__(x,y)
    self.tipo='Triangulo_'
    self.num=0

    def info(self):
        return{'Area',self.area,'Perimetro ',self.perimetro}

def Quadrado(Poligono):
    def __init__(self,x,y):
        super().__init__(x,y)
    self.tipo='Quadrado_'
    self.num=0
    
    def info(self):
        return{'Area',self.area,'Perimetro ',self.perimetro}
