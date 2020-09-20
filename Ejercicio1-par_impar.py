n1 = input("Ingrese el 1º número")
assert n1.isdigit(), "debe ser un número "
nn1=int(n1)
if nn1 % 2 == 0:
    print(nn1,"Es es par")
n2 = int(input("Ingrese el 2º número"))
if n2 % 2 > 0:
    print(n2,"Es es impar")
