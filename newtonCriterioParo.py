# Autores: Mercedes Miranda 
#          El nombre de tu amigo
# Fecha; 9 de septiembre de 2019
# Metodo Newton Raphson

import sympy as sym
#se define el simbolo variable principal, no mover
x = sym.Symbol('x')
#se define la funcipon para desarrollar el metodo
#funcion es la función en terminos de sympy, trataré de agregar un apendice
#de funciones posibles que se pueden agregar
#x0 es el valor semilla, tomar las consideraciones necesarias para ello
#errorRelativo es el criterio de paro dado por el usuario
#es importante tener en cuenta que las iteraciones seran pocas debido a la 
#eficacia del metodo
def newton(funcion,x0,errorRelativo,digitos):
    #se calcula la derivada y la division de f(x)/f'(x)
    derivada   = funcion.diff(x,1)
    diferencia=funcion/derivada
    #se muestra la division
    print("h(x) = f(x)/f'(x)")
    print("h(x) = ",diferencia)
    
    #variable auxiliar para las iteraciones
    iteracion=0
    banderaConvergencia=0
    #listas para guardar la información
    valoresAproximados=[x0]
    valoresErrorRelativo=['-']
    criterioDeConvergencia=[round(CriterioConvergencia(funcion,x0),digitos)]
    
    while(True):
        #se calcula la aproximacion
        xAnterior=x0
        a=diferencia.subs(x,x0)
        a=x0-a.evalf()
        x0=round(a,digitos)
        valoresAproximados.append(x0)
        
        #si estamos en una iteracion diferente a la primera, se calcula el 
        #error relativo
        if(iteracion!=0):
            errorR=round((abs((x0-xAnterior)/x0))*100,digitos)
            valoresErrorRelativo.append(errorR)
            #si se cumple el criterio de paro, sale de las iteraciones
            if(errorR<errorRelativo):
                break
        #se calcula el valor de convergencia
        valorG=round(CriterioConvergencia(funcion,x0),digitos)
        criterioDeConvergencia.append(valorG)
        #se checa si el valor cumple o no lo especificado
        if abs(valorG)>1:
            banderaConvergencia=1
            break
        
        #se incrementa en 1 el contador de iteraciones
        iteracion+=1
    #se retornan todas las listas y el valor de la bandera
    return valoresAproximados,valoresErrorRelativo,criterioDeConvergencia,banderaConvergencia

#esta función evalua para el criterio de convergencia en cada aproximación generada y regresa
#el valor de la evaluación de |G'(x)|                
def CriterioConvergencia(funcion,x0):
    #se calculan las dos derivadas
    derivada   = funcion.diff(x,1)
    derivadaDos = funcion.diff(x,2)
    #se genera a la función G'(x)
    G=(funcion*derivadaDos)/(derivada**2)
    #se evalua para la raiz encontrada
    a=G.subs(x,x0)
    a=a.evalf()
    
    return a

#solo genera la grafica de la funcion
def Grafica(funcion):
    grafica=sym.plotting.plot(funcion,show=True)

#función maestra
def main():
    #la función se muestra aquí
    funcion=sym.cos(x)-(x**2)
    #si quieres que el usuario ingrese la función, descomenta las lineas entre
    #signos de suma y comenta la linea de arriba de "funcion"
    #recuerda usar la documentación para saber como ingresar ciertas funciones
    #++++++++++++++++++++++++++
    #funcion=input("ingresa la función en terminos de x")
    #++++++++++++++++++++++++++
    
    #grafica
    Grafica(funcion)
    #criterio de paro
    errorRelativo=float(input("introduce el porcentaje de error para el criterio de paro "))
    #valor semilla
    semilla=float(input("ingresa el valor semilla "))
    #cantidad de digitos al redondear
    digitos=int(input("cantidad de digitos de redondeo, hasta 8 permitidos "))
    
    #se generan todos los valores necesarios para desplegar la tabla
    valores,errores,criterios,bandera=newton(funcion,semilla,errorRelativo,digitos)
    #se imprimen los valores
    print("{:2}|{:^12}|{:^12}|{:^12}|{:^12}".format("I","xi","xi+1","ErrorR","CritConv"))
    for i in range(len(valores)-1):
        print("{:2}|{:12}|{:12}|{:12}|{:12}".format(i+1,valores[i],valores[i+1],errores[i],criterios[i]))
    #hasta acá es donde se checa el criterio de convergencia    
    if bandera==1 :
        print("hubo un problema con el criterio de paro en la ultima iteración, quizá por esto terminó el proceso")
        print("revisa tu valor semilla e intenta con otro ")
        
main()
        
        
        
        
        
        