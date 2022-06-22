#Este codigo imprime una lista de 500 numeros

import random
from itertools import count

def count_aleat():
    lista = [] #Este es para que quede en lista
    inicio = 0 #Estas dos variables son de count()
    paso = 1
    contador = count(inicio , paso)
    for n in contador:# Aqui n hace el trabajo duro
        i = random.randint(0, 500)# Aqui la i busca los numeros aleatorios
        lista.append(i)
        if n > 500:
            break
    print(lista)
    print("El contador ha finalizado")
        
       
        
count_aleat()
