import matplotlib.pyplot as plt

class RK2:
    Zderivada='24*x**2'
    Yderivada='z'
    #valores que se inician al crear un objeto nuevo
    x=[]
    y=[]
    z=[]
    F=[]
    h=0.3
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
        self.y=[0]
        self.z=[-3]
        #se define el vector F que es la función de cada una de las derivadas
        #de las variables arriba descritas, se ponen en vorma de cadena para
        #operarlas mediante el comando eval, haciendo dinamico este problema
        #podiendo agregar cualquier tipo de ecuacion
        self.F=['z','24*(x**2)']
        #se agregan los valores iniciales en la lista de tiempos y de valores
        #en equis para su posteriror ploteo
        #self.graf.append(self.x)
        #self.grafx.append(self.y[0])
        #self.grafxanalitica.append(self.y[0])**********************************************
        
    def Fcalcula(self,x,y,z):
        resultado=[]
        for f in self.F:
            resultado.append(eval(f))
        #se regresa una lista de resultados de evaluar F(t,Y)
        return resultado
    
    def kUno(self):
        k1=[]
        x=self.x[len(self.x)-1]
        y=self.y[len(self.y)-1]
        z=self.z[len(self.z)-1]
        
        Fevaluada=self.Fcalcula(x,y,z)
        for f in Fevaluada:
            k1.append(f*self.h)
        self.k1=k1
        
    def kDos(self):
        k2=[]
        x=self.x[len(self.x)-1]+self.h
        y=self.y[len(self.y)-1]+self.k1[0]
        z=self.z[len(self.z)-1]+self.k1[1]
        Fevaluada=self.Fcalcula(x,y,z)
        for f in Fevaluada:
            k2.append(f*self.h)
        self.k2=k2
        
    def NuevaY(self):
        self.y.append(self.y[len(self.y)-1]+((1/2)*(self.k1[0]+self.k2[0])))
        self.z.append(self.z[len(self.z)-1]+((1/2)*(self.k1[1]+self.k2[1])))
        #self.xA=math.cos(self.t)+math.sin(self.t)
        
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
        self.NuevaY()
        self.x.append(round(self.x[len(self.x)-1]+self.h,1))
        
        
class RK4:
    Zderivada='24*x**2'
    Yderivada='z'
    #valores que se inician al crear un objeto nuevo
    x=[]
    y=[]
    z=[]
    F=[]
    h=0.3
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
        self.y=[0]
        self.z=[-3]
        #se define el vector F que es la función de cada una de las derivadas
        #de las variables arriba descritas, se ponen en vorma de cadena para
        #operarlas mediante el comando eval, haciendo dinamico este problema
        #podiendo agregar cualquier tipo de ecuacion
        self.F=['z','24*(x**2)']
        #se agregan los valores iniciales en la lista de tiempos y de valores
        #en equis para su posteriror ploteo
        #self.graf.append(self.x)
        #self.grafx.append(self.y[0])
        #self.grafxanalitica.append(self.y[0])**********************************************
        
    def Fcalcula(self,x,y,z):
        resultado=[]
        for f in self.F:
            resultado.append(eval(f))
        #se regresa una lista de resultados de evaluar F(t,Y)
        return resultado
    
    def kUno(self):
        k1=[]
        x=self.x[len(self.x)-1]
        y=self.y[len(self.y)-1]
        z=self.z[len(self.z)-1]
        
        Fevaluada=self.Fcalcula(x,y,z)
        for f in Fevaluada:
            k1.append(f*self.h)
        self.k1=k1
        
    def kDos(self):
        k2=[]
        x=self.x[len(self.x)-1]+self.h/2
        y=self.y[len(self.y)-1]+self.k1[0]/2
        z=self.z[len(self.z)-1]+self.k1[1]/2
        Fevaluada=self.Fcalcula(x,y,z)
        for f in Fevaluada:
            k2.append(f*self.h)
        self.k2=k2
        
    def kTres(self):
        k3=[]
        x=self.x[len(self.x)-1]+self.h/2
        y=self.y[len(self.y)-1]+self.k2[0]/2
        z=self.z[len(self.z)-1]+self.k2[1]/2
        
        Fevaluada=self.Fcalcula(x,y,z)
        for f in Fevaluada:
            k3.append(f*self.h)
        self.k3=k3
        
    def kCuatro(self):
        k4=[]
        x=self.x[len(self.x)-1]+self.h
        y=self.y[len(self.y)-1]+self.k3[0]
        z=self.z[len(self.z)-1]+self.k3[1]
        
        Fevaluada=self.Fcalcula(x,y,z)
        for f in Fevaluada:
            k4.append(f*self.h)
        self.k4=k4
        
    def NuevaY(self):
        self.y.append(self.y[len(self.y)-1]+(1/6)*(self.k1[0]+2*self.k2[0]+2*self.k3[0]+self.k4[0]))
        self.z.append(self.z[len(self.z)-1]+(1/6)*(self.k1[1]+2*self.k2[1]+2*self.k3[1]+self.k4[1]))
        #self.xA=math.cos(self.t)+math.sin(self.t)
        
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
        
def ecuacionReal(valores):
    lista=[]
    for x in (valores):
        lista.append(eval('2*x**4-3*x'))
    return lista


rk2=RK2()
rk4=RK4()
for i in range(10):
            rk2.itera()
            rk4.itera()
lista=ecuacionReal(rk2.x)
           
#texto='+-------------------------------------------------------------------------+\n'
#texto+='{0}{1:>7}{0}{2:>21}{0}{3:>21}{0}{4:>21} \n'.format('|','Tiempo','Solucion RK2','Solucion RK4','solucion real')
#texto+='+-------------------------------------------------------------------------+\n'
#for i in range(10):
#    texto+='{0}{1:>7}{0}{2:>21}{0}{3:>21}{0}{4:>21} \n'.format('|',rk2.x[i],rk2.y[i],rk4.y[i],lista[i])
#print(texto)

texto='+-------------------------------------------------------------------------+\n'
texto+='|Tiempo | Solucion RK2        |Solución RK4         |Solcuion Real'
texto+='+-------------------------------------------------------------------------+\n'
for i in range(10):
    texto+='|'+str(rk2.x[i])+'|'+str(rk2.y[i])+'|'+str(rk4.y[i])+'|'+str(lista[i])+'\n'
print(texto)

fig = plt.figure(figsize=(10,6))
plt.title("Grafica comparativa")
plt.xlabel("Tiempo T")
plt.ylabel("Posicion en X")
plt.grid()   
plt.plot(rk2.x,rk2.y,'r*-',label="solucion con RK2")
plt.plot(rk4.x,rk4.y,'bo-',label="solucion con RK4")
plt.plot(rk4.x,lista,'go-',label="solucion real")
plt.legend(loc="upper left")
plt.show()
#plt.savefig("picturename.png")


        
        
        
        
        
        
        