# hacer un juego de piedra papel o tijera x
# pedir que elija piedra papel o tijera x
# elegir aleatoriamente piedra papel o tijera x
# comparar con el valor del usuario x
# hacer que el valor del usuario sea aleatorio?
# agregar sentencia  while y try

import random
print("Bienvenido al juego de piedra, papel o tijera.")
valor = input("Elije piedra, papel o tijera: ")
Naleatorio = random.randint(0, 10)


def juego(valor, Naleatorio):
    if Naleatorio <= 3:
        print()
        mano = 'piedra'
        print("Has elegido: " + valor)
        print('La maquina saco: piedra')
    elif Naleatorio <= 6:
        print()
        mano = 'tijera'
        print("Has elegido: " + valor)
        print('La maquina saco: tijera')
    elif Naleatorio > 6:
        print()
        mano = 'papel'
        print("Has elegido: " + valor)
        print("La maquina saco: papel")
    if mano == valor:
        print()
        return ('Empataron')
    elif valor == 'piedra' and mano == 'tijera':
        print()
        return ('Te felicito ganaste !!')
    elif valor == 'tijera' and mano == 'papel':
        print()
        return ('Te felicito ganaste !!')
    elif valor == 'papel' and mano == 'piedra':
        print()
        return ('Te felicito ganaste !!')
    else:
        print()
        return ('Lo siento, perdiste =(')


ppt = juego(valor, Naleatorio)
print(ppt)

print(Naleatorio)
