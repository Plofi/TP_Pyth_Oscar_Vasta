# Oscar Vasta Guia de Ejercicios 1.3 
""" UN PROGRAMA QUE  CALCULA EL PERIMETRO Y AREA DE UN RECTÁNGULO  EN BASE A LAS DIMENSIONES 
DE BASE Y ALTURA Y TAMBIEN CALCULA LA SUPERFICIE Y AREA DE UN RECTÁNGULO EN BASE A LOS EJES 
DEFINIDOS POR LOS PUNTOS  x1-x2 E y1-y2 """ 
def rectdim(b, a):
    perec = (abs(b) * 2) + (abs(a) * 2)
    suprec = (abs(a) * abs(b))
    return perec, suprec
""" lo de los valores absolutos es por que seria muy facil ingrasar valores negativos, 
    sobre todo por que los puntos de los ejes podrian estan en los cuadrantes 2, 3 o 4 
    pero los perímetros y las superficies siempre son magnitudes positivas """
def receje(u, v, w, x):
    ejeab = abs(v - u)
    ejeor = abs(x - w)
    perec = (ejeab * 2) + (ejeor * 2)
    suprec = ejeab * ejeor
    return perec, suprec

print('_'*105)
print()
print(' 1º PARTE DEL PROGRAMA : calcula el perimetro y superficie de un rectangulo en base a dimensiones base y altura ')
print('( Nota: si ingresa valores decimales use punto < . > decimal ) ' )
print()
xx = input("ingrese base del rectangulo [m] : ")
x=float(xx)
yy = input("ingrese altura del rectángulo [m] : ")
y=float(yy)
print()
print('El perímetro y la superficie del rectángulo son : ', rectdim(x,y), '[m] y [m2] respectivamente')
print()
print('_'*105)
print()
print(' 2º PARTE DEL PROGRAMA : calcula el perimetro y superficie de un rectangulo en base a los') 
print(' puntos inicial y final del eje de absisas y los puntos inicial y final del eje de ordenadas ')
print()
x1 = float(input("ingrese el punto x1 (o punto inicial del eje de absisas)   [cm]: "))
x2 = float(input("ingrese el punto x2 (o punto final del eje de absisas)     [cm]: "))
y1 = float(input("ingrese el punto y1 (o punto inicial del eje de ordenadas) [cm]: "))
y2 = float(input("ingrese el punto y2 (o punto final del eje de ordenadas)   [cm]: "))
print()
print('El perímetro y la superficie del rectángulo son : ', receje(x1,x2,y1,y2), ' [cm] y [cm2] respectivamente')
print()
print('_'*105)
# - END OF FILE -





