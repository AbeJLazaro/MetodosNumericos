import matplotlib.pyplot as plt
class RK4:
    #valores que se inician al crear un objeto nuevo
    x=[]
    y=[]
    z=[]
    F=[]
    h=0.1
    #valores dinamicos, estos son auxiliares para encontrar a y
    x=0
    k1=[]
    k2=[]
    #k3=[]
    #k4=[]
    #valores para graficar
    valoresy=[]
    valoresx=[]
    def __init__(self):
        #se agrega en el vector(lista) y los valores iniciales tomando en cuenta que
        #la primer posición es la variable x y la segunda es la variable y
        self.x=[0]
        self.y=[2]
        #self.z=[2]
        #se define el vector F que es la función de cada una de las derivadas
        #de las variables arriba descritas, se ponen en vorma de cadena para
        #operarlas mediante el comando eval, haciendo dinamico este problema
        #podiendo agregar cualquier tipo de ecuacion
        self.F=['((5/4)*y)+((x*y)/4)']
        #se agregan los valores iniciales en la lista de tiempos y de valores
        #en equis para su posteriror ploteo
        #self.graf.append(self.x)
        #self.grafx.append(self.y[0])
        #self.grafxanalitica.append(self.y[0])**********************************************
        
    def Fcalcula(self,x,y):
        resultado=[]
        for f in self.F:
            resultado.append(eval(f))
        #se regresa una lista de resultados de evaluar F(t,Y)
        return resultado
    
    def kUno(self):
        k1=[]
        x=self.x[len(self.x)-1]
        y=self.y[len(self.y)-1]
        
        Fevaluada=self.Fcalcula(x,y)
        for f in Fevaluada:
            k1.append(f*self.h)
        self.k1=k1
        
    def kDos(self):
        k2=[]
        x=self.x[len(self.x)-1]+self.h/2
        y=self.y[len(self.y)-1]+self.k1[0]/2
        Fevaluada=self.Fcalcula(x,y)
        for f in Fevaluada:
            k2.append(f*self.h)
        self.k2=k2
        
    def kTres(self):
        k3=[]
        x=self.x[len(self.x)-1]+self.h/2
        y=self.y[len(self.y)-1]+self.k2[0]/2
        
        Fevaluada=self.Fcalcula(x,y)
        for f in Fevaluada:
            k3.append(f*self.h)
        self.k3=k3
        
    def kCuatro(self):
        k4=[]
        x=self.x[len(self.x)-1]+self.h
        y=self.y[len(self.y)-1]+self.k3[0]
        
        Fevaluada=self.Fcalcula(x,y)
        for f in Fevaluada:
            k4.append(f*self.h)
        self.k4=k4
        
    def NuevaY(self):   
        self.y.append(self.y[len(self.y)-1]+(1/6)*(self.k1[0]+2*self.k2[0]+2*self.k3[0]+self.k4[0]))
        
        
    #se define la funcion itera para poder ocupar hacer uso de las funciones anteriores.
    #Las funciones anteriores no necesitan parametros mas que Fcalcula, esto es a lo que
    #pretendia llegar al usar el paradigma oriendato a objetos para no estar batallando
    #con saber que valores pasar a las funciones en una funcion global main como
    #la que se ve a continucacion.
    #Se define una nueva t, se generan las K's y posterior se genera la nueva y
    #al final estos valores se agregan a las listas para su ploteo
    def itera(self):
        self.kUno()
        self.kDos()
        self.kTres()
        self.kCuatro()
        self.NuevaY()
        self.x.append(round(self.x[len(self.x)-1]+self.h,1))
        
class Euler:
    x=[]
    y=[]
    F=[]
    h=0.1
    
    def __init__(self):
        self.x.append(0)
        self.y.append(2)
        self.F=['((5/4)*y)+((x*y)/4)']
    
    def Fcalcula(self,x,y):
        resultado=[]
        for f in self.F:
            resultado.append(eval(f))
        #se regresa una lista de resultados de evaluar F(t,Y)
        return resultado
    
    def itera(self):
        ultimay=self.y[len(self.y)-1]
        ultimax=self.x[len(self.x)-1]
        fx=self.Fcalcula(ultimax,ultimay)
        fx=fx[0]
        aux=ultimay+(fx*self.h)
        fxi=self.Fcalcula(ultimax+self.h,aux)
        fxi=fxi[0]
        nuevay=ultimay+(self.h/2)*(fx+fxi)
        self.y.append(nuevay)
        self.x.append(ultimax+self.h)
        

rk4=RK4()
eu=Euler()
for i in range(20):
            rk4.itera() 
            eu.itera()
texto='+-------------------------------------------------------------------------+\n'
texto+='{0}{1:>7}{0}{2:>21}{0}{3:>21}{0}{4:>23}{0}{5:>21} \n'.format('|','Tiempo','Solucion RK4','Solucion euler','error absoluto','error porcentual')
texto+='+-------------------------------------------------------------------------+\n'
for i in range(21):
    errorAbsoluto=abs((rk4.y[i]-eu.y[i])/rk4.y[i])
    errorRelativo=errorAbsoluto*100
    texto+='{0}{1:>7}{0}{2:>21}{0}{3:>21}{0}{4:>23}{0}{5:>21} \n'.format('|',rk4.x[i],rk4.y[i],eu.y[i],errorAbsoluto,errorRelativo)
print(texto)


        
fig = plt.figure(figsize=(10,6))
plt.title("Grafica comparativa")
plt.xlabel("Tiempo T")
plt.ylabel("Posicion en X")
plt.grid()   
plt.plot(rk4.x,rk4.y,'bo-',label="solucion con RK4")
plt.plot(eu.x,eu.y,'go-',label="solucion con euler")
plt.legend(loc="upper left")
plt.show()