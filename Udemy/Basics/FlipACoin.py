# pedir que elija cara o cruz x
  #asignarle un valor (1 o 0) x
# generar numero aleatorio x
# comparar el Nº del usuario con el obtenido x
# agregar un segundo usuario?
# crear excepciones
# agregar funcion while y try

def caraocruz(valor, Naleatorio):
    if valor == "cara":
      valor = 1
    if valor =="cruz":
      valor = 0
    else:
      print("Escribe solo ´cara´ o ´cruz´")
    if valor == Naleatorio and Naleatorio == 1:
      return("Salio cara, Ganaste")
    if valor == Naleatorio and Naleatorio == 0:
      return("Salio cruz, Ganaste")
    else:
      return("Lo siento, Perdiste")



import random
print("Bienvenido al juego de cara o cruz")
while True:
  valor = input("Elije cara o cruz: ")
  Naleatorio = random.randint(0,1)
  juego = caraocruz(valor, Naleatorio)
  print(juego)
  print()
  loop = input("Deseas seguir jugando? si/no: ")
  if loop != "si":
    print("Gracias por jugar")
    break;
print()