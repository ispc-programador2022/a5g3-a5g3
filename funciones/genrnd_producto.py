from genrnd import*

lista = genrnd()

def multiplicar (valores):
    for i in range (len(lista)):
        a = lista [i]
        for e in range (len(lista)):
            b = lista [e]
            combinacion = a*b
            print (combinacion)

multiplicar(lista)
