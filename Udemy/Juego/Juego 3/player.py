class Player:
    vocation = 'No vocation'
    spell = 'No spell'
    movement_speed = 50
    atack = 40
    hitpoints=50
    mana=50

    def __init__(self, **kwargs):
        
        self.name = input('Escribe tu nombre: ')

    def __str__(self):
        return '{} es un {} tiene {} puntos de vida y {} de mana, puede lanzar {},se mueve a {} clicks y tiene {} puntos de ataque'.format(
            self.name, self.vocation, self.mana, self.hitpoints, self.spell,
            self.movement_speed,
            self.atack)


class Druid(Player):
    hitpoints= 60
    mana=80
    vocation = 'Druid'
    spell = 'Curatio'
    movement_speed = 40
    atack=40
    type="Earth"
    vulneravility="Water"

    def combatedruida(self,enemigo,):  # Arreglar vida negativa
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
                return "Ganaste"
                break
                # else:
                # print("Ganaste")
                # break



class Knight(Player):
    hitpoints=80
    mana=40
    vocation = 'Knight'
    spell = 'Exura'
    movement_speed = 60
    atack=40
    type="Fire"
    vulneravility="Water"



class Mage(Player):
    hitpoints=50
    mana=100
    vocation = 'Mage'
    spell = 'chrono inmovili'
    movement_speed = 20
    atack=40
    type="Water"
    vulneravility="Earth"
