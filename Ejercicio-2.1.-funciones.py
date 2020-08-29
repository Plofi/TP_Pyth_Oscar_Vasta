# Ejercicio 2.2 de Oscar Vasta
# Creando funciones
#
""" Crea 3 funciones para calcular descuentos ,
La 1º funcion calcula un descuento del 10% si en el carrito hay mas de 3 ítems y si el 
total de compra supero los $10.000 se aplica el 20% de descuento, 
El 2º array aplica el descuento del costo de envío de $200 si se aplica descuento
por el 1º caso y la 3º funcion calcula el descuento por puntaje de 10 puntos por cada
item que suma 10% al descuento que se aplique. """
# carga oferta de articulos en tablas en memoria
Desc_Art=(['Pan','Fideos','Leche','Gaseosa','Cerveza','Carne Vacuna','Dentifrico','Desodorante',])
Precio_Art=([150,47,75,80,135,350,125,185])
Um_Art=(['Kgr','paquete','Litro','botella','botella','Kgr','Un','Un'])
Valor_Compra=([])
Cant_Compra=([])
sigue=''
b=int()
while sigue != 'N' and  sigue != 'n':
        # muestra los articulos y precios por pantalla
    print('ITEM | DESCRIPCIÓN |PRECIO| U/M ')
    b=0
    for a in Desc_Art:
        print(b,a,' '*(12-len(str(a))),'|',Precio_Art[b],' '*(4-len(str(Precio_Art[b]))),'|',Um_Art[b],' '*(7-len(str(Um_Art[b]))),'|')
        b+=1 
    print('su compra:',lleva_art,lleva_pes)     
    sigue=input('sigue ? <N> para terminar la compra o cualquier tecla para seguir')
#
#cont=0
#while sigue = s or sigue='S':
#    cont=++
#    Cant=input('Ingrese la cantidad de articulos del tipo: ',cont )
#def descuento_cantidad_valor()
