#polinomio de taylor
import sympy as sym
import math
#funcion que determinará los polinomios de Taylor de cierto grado
#funcionx representa la función en terminos de x
#x0 es el valor alrededor del cual se desarrollara la serie
#n es el grado maximo del polinomio al que se llegará
def taylor(funcionx,x0,n):
    k = 0
    polinomio = 0
    while (k <= n):
        derivada   = funcionx.diff(x,k)
        derivadax0 = derivada.subs(x,x0)
        divisor   = math.factorial(k)
        terminok  = (derivadax0/divisor)*(x-x0)**k
        polinomio = polinomio + terminok
        k = k + 1
    return(polinomio)

#se asigna una x como un valor string para las funciones, no tocar
x = sym.Symbol('x')

#aquí se define la función en terminos de la variable equis anteriormente
#asignada, para poner exponenciales ocupar la función math.exp(n) donde n
#es el exponente al cual se eleva e
funcionx = 1/(2-x)

a = 0        # Valor alrededor del cual se desarrolla la serie
n  = 4       # Grado polinomio Taylor
valor=3

# tabla polinomios
px_tabla = []
for grado in range(0,n,1):
    polinomio = taylor(funcionx,a,grado)
    px_tabla.append(polinomio)

# SALIDA
for grado in range(0,n,1):
    px = px_tabla[grado]
    x=valor
    solucion=eval(str(px))
    solucionreal=eval(str(funcionx))
    error=sym.Abs((solucion-solucionreal)/solucionreal)
    print("{}|{:40}|{:10}|{}".format(str(grado),str(px),str(solucion),str(error)))
