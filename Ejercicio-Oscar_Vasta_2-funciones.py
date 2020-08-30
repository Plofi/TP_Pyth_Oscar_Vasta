# Ejercicio 2.2 de Oscar Vasta
#
""" Crea 3 funciones para calcular descuentos ,
La 1º funcion calcula un descuento del 10% si en el carrito hay mas de 3 ítems y si el 
total de compra supero los $10.000 se aplica el 20% de descuento, 
El 2º array aplica el descuento del costo de envío de $200 si se aplica descuento
por el 1º caso y la 3º funcion calcula el descuento por puntaje de 10 puntos por cada
item que suma 10% al descuento que se aplique. """

# declaracion de variables y de tablas y carga datos en tablas en memoria
Desc_Art=(['Pan','Fideos','Leche','Gaseosa','Cerveza','Carne Vacuna','Dentifrico','Desodorante',])
Precio_Art=([150,47,75,80,135,350,125,185])
Um_Art=(['Kgr','paquete','Litro','botella','botella','Kgr','Un','Un'])
Valor_Compra=([])
Cant_Compra=([])
sigue=''
b=int()
carrito_cant=int()
carrito_suma=int()
sucompra=int()
item=int()
cantidad=int()

# declaracion de funciones
def muestralista():
    # muestra los articulos y precios por pantalla
    print('I | DESCRIPCIÓN   |PRECIO | U/M      |')
    b=0
    for a in Desc_Art:
        print(b,'|',a,' '*(12-len(str(a))),'|',Precio_Art[b],' '*(4-len(str(Precio_Art[b]))),'|',Um_Art[b],' '*(7-len(str(Um_Art[b]))),'|')
        b+=1  

def cantcarrito(cantidad):
    if cantidad > 0:
        Cant_Compra.append(cantidad)
        return sum(Cant_Compra)
    else:
        return 0

def valcarrito(item,cantidad):
    if cantidad >0 and item <= len(Desc_Art):
        Valor_Compra.append(Precio_Art[item]*cantidad)
        return sum(Valor_Compra)
    else:
        return 0
 

# lazo principal de ejecucion del programa 
while sigue != 'N' and  sigue != 'n':
    muestralista()
    print('su compra:',cantcarrito(cantidad),'articulos por valor $',valcarrito(item,cantidad))   
    sigue = input('sigue ? <N> para terminar la compra o selecciones un Nº de Item para cargar al carrito:',)
    item = int(sigue)
    print(Desc_Art[item])
    cantidad=int(input('ingrese la cantidad:',))
#
#cont=0
#while sigue = s or sigue='S':
#    cont=++
#    Cant=input('Ingrese la cantidad de articulos del tipo: ',cont )
#def descuento_cantidad_valor()
