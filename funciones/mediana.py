from genrnd import *

print (genrnd())

lista = genrnd()

def obtener_mediana(lista):
    lista.sort()
    longitud = len(lista)
    mitad = int(longitud / 2)
    if longitud % 2 == 0:
        mediana = (lista[mitad - 1] + lista[mitad]) / 2
    else:
        mediana = lista[mitad]
    return mediana

print(obtener_mediana(lista))

