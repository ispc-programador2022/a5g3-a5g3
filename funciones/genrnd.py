import random

def genrnd():
    """retorna una lista con 50 números aleatorios"""
    
    cant_numeros = 50 # cantidad de números a generar
    desde = 1
    hasta = 1000

    lista = []
    for i in range(cant_numeros):
        num_aleatorio = random.randint(desde, hasta)
        lista.append(num_aleatorio)
    
    return lista
