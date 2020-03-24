class Player:
    vocation = 'No vocation'
    spell = 'No spell'
    movement_speed = 50

    def __init__(self,**kwargs):
        self.hitpoints = kwargs.get('hitpoint',50)
        self.mana = kwargs.get('mana',50)
        self.name = input('Escribe tu nombre: ')

    def __str__(self):
        return '{} es un {} tiene {} puntos de vida y {} de mana, puede lanzar {} y moverse a {} clicks'.format(self.name,
                                                                                                                self.vocation,
                                                                                                                self.mana,
                                                                                                                self.hitpoints,
                                                                                                                self.spell,
                                                                                                                self.movement_speed)


class Druid(Player):
    vocation = 'Druid'
    spell = 'Curatio'
    movement_speed = 40

class Knight(Player):
    vocation = 'Knight'
    spell = 'Exura'
    movement_speed = 60

class Mage(Player):
    vocation = 'Mage'
    spell = 'chrono inmovili'
    movement_speed = 20
