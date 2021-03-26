#Gauss Jordan
import numpy as np

#impresion del sistema, esta función es recurrente, por ello se decidió definirla
#para poder ver como se comporta el sistema tras cada iteración
def PrintSistema(matriz,vector):
    #se encuentran las dimensiones de la matriz para saber cuantos renglones tiene
    dimensiones=matriz.shape
    #en un ciclo se imprime el renglon de la matriz de coeficientes con el valor
    #correspondiente del vector de soluciones
    for i in range(dimensiones[0]):
        print(str(matriz[i])+" ["+str(vector[i])+"]")
    print("\n")
    
#importando datos
def MatrizCoeficientes(renglones,columnas):
    #se genera una matriz de ceros y un vector de ceros de una cantidad determinada
    #e columnas y renglones
    matrizCoef=np.zeros((renglones,columnas))
    vectorSolucion=np.zeros(renglones)
    #en un ciclo doble, se piden los valores de cada coeficiente y del correspondiente
    #digito del vector de soluciones
    for i in range(renglones):
        print("ingresa los coeficientes de la ecuacion "+str(i+1))
        for j in range(columnas):
            matrizCoef[i,j]=float(input())
        vectorSolucion[i]=float(input("solucion "))
    #se imprime el sistema y se regresa la matriz junto con el vector
    print("\n")
    PrintSistema(matrizCoef,vectorSolucion)    
    return matrizCoef,vectorSolucion

#acomodar renglones a partir del pivote-columna
def AcomodarRenglones(inicio,renglones,columna,matriz,vector):
    #en una forma de ordenamiento burbuja, se acomodan los renglones de acuerdo
    #al valor que tienen en una columna indicada, también se acomoda en el vector
    #de soluciones
    for i in range(inicio,renglones):
        for j in range(i+1,renglones):
            #la condicion es si el valor absoluto del termino n del renglon original
            #es mayor, se intercambia con el renglon que tenga un valor absoluto
            #menor en el termino n, de tal modo que siempre arriba quede el de menor
            #valor para que las restas no sean tan pesadas.
            #también se evita tener un pivote cero con la segunda condición que indica
            #que se intercambiaran si el valor del termino n del renglon original es 
            #cero
            if abs(matriz[i,columna])>abs(matriz[j,columna]) or matriz[i,columna]==0:
                #se verifica que el valor a cambiar no sea cero, evitando la problematica
                #de arriba
                if (matriz[j,columna]!=0):
                    #se imprime un mensaje-bandera
                    print("intercambio de renglones entre "+str(i+1)+" y "+str(j+1))
                    #se muestran los valores antes y despues del cambio
                    PrintSistema(matriz,vector)
                    #así se intergambian renglones con numpy
                    matriz[[i,j],:]=matriz[[j,i],:]
                    #asignación simultanea de python para una lista
                    vector[i],vector[j]=vector[j],vector[i]
                    PrintSistema(matriz,vector)
                    
#función para normalizar el renglon de acuerdo a su valor pivote
def Normalizar(renglon,columna,matriz,vector):
    #se verifica que el valor pivote no sea ya sero, de serlo, no se hace nada
    #para evitar operaciones inecesarias
    if matriz[renglon,columna]!=1:
        #se encuentra el factor de normalización que es el mismo pivote
        factor=matriz[renglon,columna]
        #se imprime un mensaje bandera
        print("Se normaliza el renglon "+str(renglon+1)+" , se divide entre "+str(factor))
        #se muestran los valores antes y después del cambio en la matriz y el vector
        #de soluciones
        PrintSistema(matriz,vector)
        matriz[renglon]=matriz[renglon]/factor
        vector[renglon]=vector[renglon]/factor
        PrintSistema(matriz,vector)
        
#aquí se hace la resta de los escalonamientos hacia abajo 
def RestaPorPivote(renglon,renglones,columna,matriz,vector):
    #se recorren todos los renglones con una columna especifica que nos determina
    #el pivote
    for i in range(renglones):
        #si el renglon en la iteración es el mismo renglon del pivote, se salta
        #dicha iteración para evitar hacerlo cero
        if i == renglon:
            continue
        #en otro caso, se encuentra el factor que es el numero debajo del pivote,
        #en la misma columna pero en distintos renglones, se multiplica al
        #renglon del pivote por este factor
        factor=matriz[i,columna]
        #mensaje bandera
        print("se multiplica el renglon "+str(renglon+1)+" por el factor "+str(factor)+" y se resta al renglon "+str(i+1))
        #se muestran los valores antes y después del los cambios
        PrintSistema(matriz,vector)
        matriz[i]=matriz[i]-(matriz[renglon]*factor)
        vector[i]=vector[i]-(vector[renglon]*factor)
        PrintSistema(matriz,vector)
        
#verificar si algun renglon es igual a cero
def MiRenglonCeros(matriz,i):
    #encuentra las dimensiones de la matriz
    dimensiones=matriz.shape
    #genera un renglon de puros ceros como comparativo, del mismo tamaño que
    #los renglones de la matriz
    comparativo=np.zeros(dimensiones[1])
    #se comparan los renglones, el de ceros y el indicado por el indice i para
    #comprobar si se trata de un renglon de puros ceros
    if np.array_equal(matriz[i],comparativo):
        return 1
    return 0

#para eliminar los renglones con puros ceros
def QuitaRenglonesCeros(matriz,vector):
    #se encuentran las dimensiones de la matriz, se hace un renglon de puros 
    #ceros como arriba para compararse
    dimensiones=matriz.shape
    comparativo=np.zeros(dimensiones[1])
    #se inicia una lista para agregar el indice de todos los renglones que tengan
    #puros ceros
    renglonesCeros=[]
    #se busca todos los renglones con ceros y se guardan sus indices
    for i in range(dimensiones[0]):
        if np.array_equal(matriz[i],comparativo):
            renglonesCeros.append(i)
    #si existe algún renglon con puros ceros, entra a eliminarlos
    if len(renglonesCeros)!=0:
        #mensaje bandera
        print("se quitaran los renglones con puros ceros")
        #se muestra la matriz y el vector de soluciones antes y después de los
        #cambios
        PrintSistema(matriz,vector)
        #así se eliminan renglones en numpy
        #matriz=np.delete(matriz,renglonesCeros,0)***************************************************
        
        mask = np.ones(len(matriz), dtype=bool)
        mask[renglonesCeros] = False
        matriz = matriz[mask,...]
        #así se trunca el vector de soluciones
        vector=vector[:len(vector)-len(renglonesCeros)]
        PrintSistema(matriz,vector)  
    return matriz,vector
        
#función que escalona los valores de la matriz y del vector de soluciones
def Escalonar(renglones,columnas,matriz,vector):
    #se inicia una variable j en 0 para las columnas en caso de que sea diferente
    #el numero de columnas y renglones
    j=0
    #se itera por renglon
    for i in range(renglones):
        #se llama a la función AcomodarRenglones para dejar el del pivote mas
        #chico hasta arriba y para evitar pivotes con el valor cero
        AcomodarRenglones(i,renglones,j,matriz,vector)
        #se busca si este renglon visto es de puros ceros, los renglones con ceros
        #quedaran hasta abajo garantizando que se puede reducir todos los demas renglones
        renglonCeros=MiRenglonCeros(matriz,i)
        if renglonCeros==1:
            print("al menos un renglon se formó de puros ceros, revisa tu sistema de ecuaciones, el ingresado es linealmente dependiente")
            break
        #en caso de no ser un renglon de puros ceros, se normaliza para tener un pivote de valor 1
        Normalizar(i,i,matriz,vector)
        #se llama a la función RestaPorPivote para eliminar valores en los demás renglones
        RestaPorPivote(i,renglones,j,matriz,vector)
        #aumenta el valor de la columna
        j+=1
        
#función para mostrar resultados        
def MostraSoluciones(matriz,vector):
    if (len(matriz)==len(matriz[0])):
        print("el sistema tiene soluciones unicas, se muestran: ")
        for i in range(len(matriz)):
            solucion=vector[i]/matriz[i,i]
            print("x"+str(i+1)+" = "+str(solucion))    
    else:
        print("el sistema no tiene soluciones unicas, no se pueden dar resultados concretos")

def main():
    cantRenglones=int(input("ingresa la cantidad de renglones "))
    cantColumnas=int(input("ingresa la cantidad de columnas "))
    print("*******************************************************")
    matrizM,vectorB=MatrizCoeficientes(cantRenglones,cantColumnas)
    Escalonar(cantRenglones,cantColumnas,matrizM,vectorB)
    matrizM,vectorB=QuitaRenglonesCeros(matrizM,vectorB)
    print("*******************************************************")
    MostraSoluciones(matrizM,vectorB)
main()