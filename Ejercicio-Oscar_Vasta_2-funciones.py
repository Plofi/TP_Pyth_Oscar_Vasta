# Ejercicio 2.2 de Oscar Vasta
""" Crea 3 funciones para calcular descuentos ,
La 1º funcion calcula un descuento del 10% si en el carrito hay mas de 3 ítems y si el 
total de compra supero los $10.000 se aplica el 20% de descuento, 
El 2º array aplica el descuento del costo de envío de $200 si se aplica descuento
por el 1º caso y la 3º funcion calcula el descuento por puntaje de 10 puntos por cada
item que suma 10% al descuento que se aplique. """

# declaracion de variables y de tablas y carga datos en tablas en memoria
Desc_Art=(['Pan','Fideos','Leche','Gaseosa','Cerveza','Carne Vacuna','Dentifrico','Desodorante','Whisky'])
Precio_Art=([150,47,75,80,135,350,125,185,980])
Um_Art=(['Kgr','paquete','Litro','botella','botella','Kgr','Un','Un','botella'])
Valor_Compra=([])
Cant_Compra=([])
sigue=''
b=int()
carrito_cant=int()
carrito_suma=int()
sucompra=int()
item=int()
cantidad=int()

# definiciones de funciones
def muestralista():
    # muestra los articulos y precios por pantalla
    print('-'*38) 
    print('I | DESCRIPCIÓN   |PRECIO | U/M      |')
    b=0
    for a in Desc_Art:
        print(b,'|',a,' '*(12-len(str(a))),'|',Precio_Art[b],' '*(4-len(str(Precio_Art[b]))),'|',Um_Art[b],' '*(7-len(str(Um_Art[b]))),'|')
        b+=1 
    print('-'*38) 

def muestrArt(it):
    if it < len(Desc_Art):
        return Desc_Art[it]
    else:
        return ''

def muestrUm(it):
    if it < len(Um_Art):
        return Um_Art[it]
    else:
        return ''

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

def descu_1(QTcarr,VTcarr):
    if VTcarr > 10000:
        return VTcarr * -0.2
    else:
        if QTcarr > 3:
            return VTcarr * -0.1
        else:
            return 0

def descu_2(descuT):
    if descuT > 0:
        return -200 
    else:
        return 0

# este no estoy muy seguro de interpretar bien el planteo
def descu_3(QTcarr,descuT):
    if QTcarr > 3:
        return descuT * 0.1 * ((QTcarr-3)) 
    else:
        return 0

# lazo principal de ejecucion del programa 
while sigue != 'N' and  sigue != 'n':
    muestralista()
    print('su compra:',cantcarrito(cantidad),'articulos por valor $',valcarrito(item,cantidad))   
    sigue = input('sigue ? <N> para terminar la compra o selecciones un Nº de Item para cargar al carrito:',)
    if sigue.isdigit():
        item = int(sigue)
        print(muestrArt(item),muestrUm(item))
        cantidad=int(input('ingrese la cantidad:',))
# vuelco de calculos a variables de total compra
if len(Cant_Compra) > 0:
    totcarr = sum(Cant_Compra)
    valcarr = sum(Valor_Compra)
    descuento_1 = descu_1(totcarr,valcarr)
    descuento_2 = descu_2(valcarr)
    # esto es para cortar en 2 decimales por que la funcion devuelve punto flotante 
    descuento_3 = int(descu_3(totcarr,descuento_1)*100)/100
    apagar = int((valcarr + descuento_1 + descuento_2 + descuento_3)*100)/100
    # excibicion de los datos finales de compra
    print()
    print('CANTIDAD TOTAL DE ARTRÍCULOS ADQUIRIDOS _____ : ',totcarr)
    print('VALOR TOTAL DE ARTÍCULOS ADQUIRIDOS _________ : $',valcarr)
    print('DESCUENTO COMPRA > 3 ARTÍCULOS O > DE $ 10000 : $',descuento_1)
    print('DESCUENTO DE TRANSPORTE _____________________ : $',descuento_2)
    print('DESCUENTO POR PUNTAJE _______________________ : $',descuento_3)
    print('TOTAL A PAGAR ________________________________: $',apagar)
else:
    print()
    print("* NO HUBO COMPRA *")
#___________________________________________________________________
# END OF FILE