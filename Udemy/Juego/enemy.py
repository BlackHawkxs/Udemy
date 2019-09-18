class Troll:
    movement_speed = 80
    spell = 'No tiene hechizo'
    type = 'Comun'

    def __str__(self):
        return 'El Trol de {} tiene {} puntos de vida y {} de mana, puede moverse a {} clicks y realizar el hechizo {}'.format(self.type,
                                                                                                                             self.life,
                                                                                                                             self.mana,
                                                                                                                             self.movement_speed,
                                                                                                                             self.spell)

    def __init__(self,**kwargs):
        self.life = kwargs.get('Life', 100)
        self.mana = kwargs.get('Mana', 100)

class Ice_troll(Troll):
    movement_speed = 90
    spell = 'Frost Byte'
    type = 'Hielo'

class Fire_troll(Troll):
    movement_speed = 50
    spell = 'Fireball'
    type = 'Fuego'

class Air_troll(Troll):
    movement_speed = 100
    spell = 'Cyclone'
    type = 'Aire'

class Earth_troll(Troll):
    movement_speed = 40
    spell = 'Earthquake'
    type = 'Tierra'


