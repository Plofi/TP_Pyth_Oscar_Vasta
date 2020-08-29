# EJERCICIO 1.1 PYTHON DE OSCAR VASTA
# UN PROGRAMA QUE PIDE AL USUARIO 3 NÚMEROS Y LOS GUARDA EN UN ARRAY
""" Si fuera necesario inicializar el arreglo en 3 elementos nulos si fuera necesario:  
        arreglo = [0 for numero in range(3)]
pero en este caso vamos a inicializar arreglo sin ningun elemento y lo vamos a ir extendiendo  """

print('.'*80)
print('-'*30+'EJERCICIO DE ARREGLO'+'-'*30)
cont = 0
numeroleido=0
arreglo=([])
while cont <= 2:
    valor = input("ingrese un número : ")
    numeroleido=int(valor)
    arreglo.append(numeroleido) 
    cont=cont+1

    """ al finalizar lel ingreso de valores vamos a mostrar el contenido del arreglo , la suma 
        , el valor mas alto y el valor mas bajo """

    if cont > 2:
        print('el arreglo es : ',arreglo,' cuya cantidad de elementos es :',len(arreglo),' y suma : ',sum(arreglo), '; el valor mas alto : ', max(arreglo), ' y el valor mas bajo : ',min(arreglo))
print('.'*80)

""" y para que al ejecutrlo desde fuera del Visual estudio Code no se desaparesca el resultado inmediatamente
 despues de ejecutar la última linea , lo detenemos preguntansdo si vio el resultado  , sal si o no """
salida = input('si vió el resultado presione cualqier tecla para salir del programa : ',)
# - END OF FILE -





