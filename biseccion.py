#bisección
import math

#la función para encontrar las raices por metodo de biseccion
#funcion es la funcion en terminos de x
#a y b son los valores del dominio tomados, del modo [a,b]
#iteraciones es la cantidad de veces que se repetira el metodo
def biseccion(funcion,a,b,iteraciones):
    for i in range(iteraciones):
        c=(a+b)/2 
        print("a: ",a)
        print("b: ",b)
        print("c: ",c)
        x=a
        valorfa=eval(funcion)
        x=b
        valorfb=eval(funcion)
        x=c
        valorfc=eval(funcion)
        print("posible raiz: "+str(c))
        if(valorfa<0):
            if(valorfc<0):
                a=c
            else:
                b=c
        if(valorfb<0):
            if(valorfc<0):
                b=c
            else:
                a=c
#funcion definida como una cadena, importante en caso de requerir e hacer uso
#de la funcion math.exp(n) donde n es el exponente al cual se eleva e
funcion='(math.exp(x-1))-1.5*x'
#cantidad de iteraciones que hará el metodo
iteraciones=10
#intervalo de valores, el menor y el mayor, es importante recordar que para
#encontrar este intervalo, es necesario hacer una breve tabulación para encontrar
#alrededor de que valores hay un cambio de signo, puesto que 
#f(a) y f(b) deben tener signos distintos
a=0
b=2
#llamada a la función
biseccion(funcion,a,b,iteraciones)