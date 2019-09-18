class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = 50
    def __init__(self,**kwargs):
        self.hitpoints = kwargs.get("hitpoints",50)
        self.mana = kwargs.get("mana", 50)
        self.name = input("Escribe tu nombre: ")

    def __str__(self):
        return "{} es un {} tiene {} puntos de vida y {} de mana, puede lanzar el hechizo {} y moverse a {} clicks".format(self.name,
                                                                                                                           self.vocation,
                                                                                                                           self.hitpoints,
                                                                                                                           self.mana,
                                                                                                                           self.spell,
                                                                                                                           self.movement_speed)

class Druid(Player):
    vocation = "Druid"
    spell = "Curatio"
    movement_speed = 40

class Paladin(Player):
    vocation = "Paladin"
    spell = "Aegis"
    movement_speed = 60

class Knight(Player):
    vocation = "Knight"
    spell = "Exura"
    movement_speed = 50





