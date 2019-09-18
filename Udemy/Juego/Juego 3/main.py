import player
import enemy


def combatedruida():  # Arreglar vida negativa
  while jugador.hitpoints > 0:
    if enemigo.element == "Agua":
        troll_health = enemigo.hitpoints - (jugador.atack * 2)
        druid_health = jugador.hitpoints - enemigo.atack
        jugador.hitpoints = druid_health
        enemigo.hitpoints = troll_health
        print("te quedan " + str(jugador.hitpoints) + " puntos de vida")
        print("Al trol le quedan " + str(enemigo.hitpoints) + " puntos de vida")

    else:
        troll_health = enemigo.hitpoints - jugador.atack
        druid_health = jugador.hitpoints - enemigo.atack
        jugador.hitpoints = druid_health
        enemigo.hitpoints = troll_health
        print("te quedan " + str(jugador.hitpoints) + "puntos de vida")
        print("Al trol le quedan" + str(enemigo.hitpoints) + "puntos de vida")
    # combat()
    if jugador.hitpoints <= 0:
      print("Perdiste")
      break
    if enemigo.hitpoints <= 0:
      print("Ganaste")
      break
      # else:
      # print("Ganaste")
      # break

print("Bienvenido al juego")
jugador = input("Puedes elegir las siguientes clases: Druida, Mago y Knight\n: ").capitalize()
if jugador == "Druida":
    jugador = player.Druid()
    tipo = 1
elif jugador == "Mago":
    jugador = player.Mage()
elif jugador == "Knight":
    jugador = player.Knight()

print("Elige el Troll a enfrentar: \n")
enemigo = input("Fuego, Agua o Tierra: \n").capitalize()
if enemigo == "Fuego":
    enemigo = enemy.Fire_troll()
elif enemigo == "Agua":
    enemigo = enemy.Ice_troll()
elif enemigo == "Tierra":
    enemigo = enemy.Earth_troll()

if tipo == 1:
    combate= combatedruida()
    
else:
    print("error")


print(enemigo)
print(jugador)
print(combate)
