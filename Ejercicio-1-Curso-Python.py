# EJERCICIO 1 PYTHON OSCAR VASTA
# UN PROGRAMA QUE PIDE AL USUARIO 3 NÚMEROS Y LOS GUARDA EN UN ARRAY
""" eso sería para inicializar el arreglo en 3 elementos nulos si fuera necesario:
 arreglo = [0 for numero in range(3)] """
cont = 0
numeroleido=0
import numpy as np
arreglo=np.array([])
while cont <= 2:
    print(arreglo)
    valor = input("ingrese un número")
    numeroleido=int(valor)
    arreglo.append(numeroleido) # esto da error " AttributeError: 'numpy.ndarray' object has no attribute 'append' "
    print(numeroleido)
    
    cont=cont+1



