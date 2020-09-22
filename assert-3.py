# ejercicio 3 de Oscar Vasta
a = input("ingrese un numero par")
try:
   A = int(a)
except Exception as e:
   print(e)
   a = 0
A = int(a)
if A/2 == A//2:
    print(A)
else:
    print('es impar')
B = int(input("ingrese unnúmero impar"))
if (B/2) != (B//2):
    print(B)
else:
    print('Es par')
# Fin
