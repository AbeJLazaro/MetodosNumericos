#secante

import math
#funcion con la que se desarrolla el metodo
#funcion es la función en terminos de x
#a es un valor de x
#b es un valor de x
#iteraciones es la cantidad de iteraciones que realizará el metodo
def secante(funcion,a,b,iteraciones):
    for i in range(iteraciones):
        x=a
        valorfa=eval(str(funcion))
        x=b
        valorfb=eval(str(funcion))
        c=a-(((b-a)/(valorfb-valorfa))*valorfa)   
        print(c)
        a,b=b,c

#la función esta definida en terminos de x, como una cadena
#aquí debes usar metodos propios de la biblioteca math
funcion='math.cos(x)-x**2'
#cantidad de iteraciones que se realizaran, es delicado este punto pues por la
#presición, en algun momento el denominador puere llegar a ser 0
iteraciones=5
#valores de x
a=2
b=1
#llamada al metodo
secante(funcion,a,b,iteraciones)