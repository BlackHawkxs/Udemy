while druid.hitpoints > 0:
  druid.atack - ice_troll.hitpoints
  else:
    return "Perdiste"


while druid.hitpoints > 0:
  ice_troll.hitpoints - druid.atack
  druid.hitpoints - ice_troll.atack  
  if druid.hitpoints == 0:
    print("Perdiste")
    break
  else:
    print("Ganaste")


  while jugador.hitpoints > 0:
  
    if enemigo.element == "Agua":
      troll_health = enemigo.hitpoints - (jugador.atack*2)
      druid_health= jugador.hitpoints - enemigo.atack
      jugador.hitpoints = druid_health
      enemigo.hitpoints = troll_health
      print(jugador.hitpoints)
      print(enemigo.hitpoints)
    else:
      troll_health = enemigo.hitpoints - jugador.atack
      druid_health= jugador.hitpoints - enemigo.atack
      jugador.hitpoints = druid_health
      enemigo.hitpoints = troll_health
      print(jugador.hitpoints)
      print(enemigo.hitpoints)
  #combat()   
  if jugador.hitpoints <= 0:
    print("Perdiste")
    break
  if enemigo.hitpoints <= 0:
    print("Ganaste")
    break
    #else:
      #print("Ganaste")
      #break

combate = enemigo.hitpoints - jugador.atack
print ("resultado del combate " +str(combate))


print("Puntos de vida del druida" + str(jugador.hitpoints))
