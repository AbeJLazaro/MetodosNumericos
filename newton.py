# Autores: Mercedes Miranda 
#          El nombre de tu amigo
# Fecha; 9 de septiembre de 2019
# Metodo Newton Raphson

import sympy as sym
#se define la funcipon para desarrollar el metodo
#funcion es la función en terminos de sympy, trataré de agregar un apendice
#de funciones posibles que se pueden agregar
#x0 es el valor semilla, tomar las consideraciones necesarias para ello
#iteraciones es la cantidad de iteraciones que se realizaran
#es importante tener en cuenta que las iteraciones seran pocas debido a la 
#eficacia del metodo
def newton(funcion,x0,iteraciones):
    derivada   = funcion.diff(x,1)
    #derivadaDos = funcion.diff(x,2)
    diferencia=funcion/derivada
    print(diferencia)
    a=x0
    for i in range(iteraciones):
        a=diferencia.subs(x,x0)
        a=x0-a.evalf()
        x0=a
        print(x0)        

#x es la variable necesitada, no mover
x = sym.Symbol('x')
#funcion en terminos de x, trataré de agregar las funciones posibles
funcion=sym.cos(x)-(x**2)
#iteraciones es la cantidad de iteraciones que se realizará
iteraciones=10
#valor semilla 
a=3

#llamada al metodo
newton(funcion,a,iteraciones)