import player
import enemy
dir(enemy)
#pjjllayer = player.Player()

#nuevo= player.Player()
druid = player.Druid(hitpoints=50, mana=80)
paladin = player.Paladin(hitpoints=80, mana=80)
knight = player.Knight(hitpoints=80, mana=60)

trolDeFuego = enemy.Fire_troll()
trolDeHIelo = enemy.Ice_troll()
trolDeTierra = enemy.Earth_troll()
trolDeAire = enemy.Air_troll()

print(knight)
print(druid)
print(paladin)

print(trolDeAire)
print(trolDeFuego)
print(trolDeHIelo)
print(trolDeTierra)
