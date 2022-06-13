#Función que retorna la potencia del primero elevado al segundo parámetro.

def potencia():
  base= int(input("Ingrese la base: "))
  exponente= int(input("Ingrese el exponente: "))
  resultado = base**exponente
  print(base,"elevado a", exponente, "es ", resultado)
