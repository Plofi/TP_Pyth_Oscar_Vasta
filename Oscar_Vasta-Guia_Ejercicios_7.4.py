"""
Oscar_Vasta-Guia_Ejercicios_7.4.py
7.4. Vectores
a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
d) Escribir una función que reciba un vector y devuelva su norma.
"""
def prodesc(v1,v2):
    c=0
    vs=()
    vsl=list(vs)
    for i in range(0,3):
        #print('*',vs[i],'* |',v1[i],'|',v2[i])
        vsl.append(v1[i]*v2[i])
    vs=tuple(vsl)
    return vs
#
def vort(v1,v2):
    c=0
    vs=()
    vsl=list(vs)
    for i in range(0,2):
        vsl.append(v1[i]*v2[i])
    vs=tuple(vsl)
    if sum(vs) == 0:
        return 'son ortogonales', True
    else:
        return 'no son ortogonales', False

# ----- programa de prueba ----
m1=(3,1,6)
m2=(9,1,5)
print()
print('_ Dados los vectores : ',m1,'y',m2)
print()
print('_ El producto escalar es : ',prodesc(m1,m2))
print()
print()
print('_ Se verifica si los mismos vectores son ortogonales en el plano X Y')
print()
print('             **  ',vort(m1,m2),'  **')


# E.O.F.
