import math
class RK4 :
    #valores que se inician al crear un objeto nuevo
    y=[]
    xA=[]
    yA=[]
    F=[]
    h=0
    #valores dinamicos, estos son auxiliares para encontrar a y
    t=0
    k1=[]
    k2=[]
    k3=[]
    k4=[]
    #listas para sacar la grafica del problema
    grafx=[]
    grafy=[]
    graft=[]
    grafxanalitica=[]
    grafyanalitica=[]
    #constructor del objeto para encontrar la solucion
    def __init__(self):
        #se agrega en el vector(lista) y los valores iniciales tomando en cuenta que
        #la primer posición es la variable x y la segunda es la variable y
        self.y=[3,6]
        #se define el vector F que es la función de cada una de las derivadas
        #de las variables arriba descritas, se ponen en vorma de cadena para
        #operarlas mediante el comando eval, haciendo dinamico este problema
        #podiendo agregar cualquier tipo de ecuacion
        self.F=['3*x-2*y','5*x-4*y']
        #se define el paso, también puedde variar
        self.h=0.2
        #se agregan los valores iniciales en la lista de tiempos y de valores
        #en equis para su posteriror ploteo
        self.graft.append(self.t)
        self.grafx.append(self.y[0])
        self.grafxanalitica.append(self.y[0])
        self.grafy.append(self.y[1])
        self.grafyanalitica.append(self.y[1])
        
    #Esta funcion funge como auxiliar que calula el vector F de cada problema,
    #haciendolo funcion y generica lo podemos usar para cualquier k cambiando
    #unicamente los valores de entrada
    def Fcalcula(self,t,x,y):
        resultado=[]
        for f in self.F:
            resultado.append(eval(f))
        #se regresa una lista de resultados de evaluar F(t,Y)
        return resultado
    
        #se regresa una lista de resultados de evaluar F(t,Y)
        return resultado
    
    #Estas funciones solo cambian en los valores de x, y y t que se definen 
    #antes de pasar los parametros a la funcion Fcalcula descrita anteriormente.
    #Esta funcion guarda dentro de los atributos del objeto los valores para
    #k1,k2,k3 y k4 para su posterior operacion sin necesidad de andar pasando
    #parametros entre ellos, tomando en cuenta el paradigma funcional dentro
    #del paradigma orientado a objetos
    def kUno(self):
        k1=[]
        x=self.y[0]
        y=self.y[1]
        t=self.t
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k1.append(f*self.h)
        self.k1=k1
        
    def kDos(self):
        k2=[]
        x=self.y[0]+self.k1[0]/2
        y=self.y[1]+self.k1[1]/2
        t=self.t+self.h/2
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k2.append(f*self.h)
        self.k2=k2
        
    def kTres(self):
        k3=[]
        x=self.y[0]+self.k2[0]/2
        y=self.y[1]+self.k2[1]/2
        t=self.t+self.h/2
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k3.append(f*self.h)
        self.k3=k3
        
    def kCuatro(self):
        k4=[]
        x=self.y[0]+self.k3[0]
        y=self.y[1]+self.k3[1]
        t=self.t+self.h
        Fevaluada=self.Fcalcula(t,x,y)
        for f in Fevaluada:
            k4.append(f*self.h)
        self.k4=k4
    #se define la función NuevaY como la función que recalcula Y con los valores
    #de k1,k2,k3 y k4 objetnidos anteriormente
    def NuevaY(self):
        for i in range(len(self.y)):
            self.y[i]=self.y[i]+(1/6)*(self.k1[i]+2*self.k2[i]+2*self.k3[i]+self.k4[i])
        e=math.e
        self.xA=2*e**(-2*self.t)+e**self.t
        self.yA=5*e**(-2*self.t)+e**self.t
            
    #se define la funcion itera para poder ocupar hacer uso de las funciones anteriores.
    #Las funciones anteriores no necesitan parametros mas que Fcalcula, esto es a lo que
    #pretendia llegar al usar el paradigma oriendato a objetos para no estar batallando
    #con saber que valores pasar a las funciones en una funcion global main como
    #la que se ve a continucacion.
    #Se define una nueva t, se generan las K's y posterior se genera la nueva y
    #al final estos valores se agregan a las listas para su ploteo
    def itera(self):
        self.t=round(self.t+self.h,1)
        self.kUno()
        self.kDos()
        self.kTres()
        self.kCuatro()
        self.NuevaY()
        self.graft.append(self.t)
        self.grafx.append(self.y[0])
        self.grafy.append(self.y[1])
        self.grafxanalitica.append(self.xA)
        self.grafyanalitica.append(self.yA)

rk4=RK4()
for i in range(10):
    rk4.itera()
    
texto='+--------------------------------------------------------------------------------------------------+\n'
texto+='{0}{1:>7}{0}{2:>21}{0}{3:>21}{0}{4:>23}{0}{5:>21} \n'.format('|','Tiempo','RK4 X','Analitica X','RK4 Y','Analitica Y')
texto+='+--------------------------------------------------------------------------------------------------+\n'
for i in range(11):
    texto+='{0}{1:>7}{0}{2:>21}{0}{3:>21}{0}{4:>23}{0}{5:>21} \n'.format('|',rk4.graft[i],rk4.grafx[i],rk4.grafxanalitica[i],rk4.grafy[i],rk4.grafyanalitica[i])
print(texto)
for i in range(10):
    print(i)