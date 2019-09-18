class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_Speed = 50

    def __str__(self):

        return "{} es un {} tiene {} puntos de vida, {} de mana, puede lanzar {} y tiene {} de velocidad de movimiento \n".format(self.name,
                                                                                                                                  self.vocation,
                                                                                                                                self.hitpoints,
                                                                                                                                self.mana,
                                                                                                                                self.spell,
                                                                                                                                self.movement_Speed)

    def __init__(self, **kwargs):  # hitpoints = 50, mana = 50, vocation ="Sorcerer", cast_spell="Puff"):
        self.hitpoints = kwargs.get("hitpoints",50)
        self.mana = kwargs.get("mana", 50)
        self.name = input('Escribe el nombre del')


class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Utevo Lux"
    movement_Speed = 40

class Knight(Player):
    vocation = "Knight"
    spell = "Exori"
    movement_Speed = 60

class Druid(Player):
    vocation = "Druid"
    spell = "Curatio"
    movement_Speed = 40


