import random

def genrnd():
    """retorna una lista con 50 números aleatorios del 1 al 100"""
    
    cant_numeros = 50 # cantidad de números a generar
    desde = 1
    hasta = 100

    lista = []
    for i in range(cant_numeros):
        num_aleatorio = random.randint(desde, hasta)
        lista.append(num_aleatorio)
    
    return lista
