#regla falsa
import math
#funcion en la que se define el metodo de la regla falsa
#función es una función en terminos de x
#a y b son intervalos en los que se puede encontrar la raiz
#iteraciones es la cantidad de iteraciones que hará el metodo
#importante recordar que este metodo tiene mayor precisión que bisección, 
#por lo tato usa menos iteraciones
def reglafalsa(funcion,a,b,iteraciones):
    for i in range(iteraciones):
        x=a
        valorfa=eval(funcion)
        x=b
        valorfb=eval(funcion)
        
        sol=a-((valorfa*(b-a))/(valorfb-valorfa))
        
        print("raiz posible: "+str(sol))
        
        if a*sol < 0 :
            b=sol
        else:
            a=sol
#función en terminos de x escrita como una cadena. En caso de requerir el termino
#e, ocupar la función math.exp(n) donde n es el exponente al cual se eleva e
funcion='math.exp(-x)-x'
#intervalos de valores, importante recordar que es necesario tabular valores
#caracteristicos o significativos para encontrar en que rango de valores cambian
#los signos de modo que f(a) y f(b) tienen signos distintos
a=0
b=1
#cantidad de iteraciones que realizará el metodo
iteraciones=10
#llamada a la función
reglafalsa(funcion,a,b,iteraciones)    