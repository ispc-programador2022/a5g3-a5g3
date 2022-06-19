import random

def super_genrnd():
    """retorna una lista con 500.000.000.000.000.000 números aleatorios del 1 al 100"""
    
    cant_numeros = 500000000000000000 # cantidad de números a generar
    desde = 1
    hasta = 100
    lista = []
    for i in range(cant_numeros):
        num_aleatorio = random.randint(desde, hasta)
        lista.append(num_aleatorio)
    print(lista)
    return lista

super_genrnd()
