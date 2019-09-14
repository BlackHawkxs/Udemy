class Troll:
    hitpoints = 100
    mana = 50
    type = 'Common'
    atack = 20
    vulneravility = 'Ninguna'

    def __str__(self):
        return 'El trol de {} tiene {} puntos de vida y {} de mana, tiene {} de ataque y es vulnerable a los ataque de {}'.format(self.type,
                                                                                                                                  self.hitpoints,
                                                                                                                                  self.mana,
                                                                                                                                  self.atack,
                                                                                                                                  self.vulneravility)


class Ice_troll(Troll):
    hitpoints = 100
    mana = 50
    type = 'Hielo'
    atack = 20
    vulneravility = 'Tierra'

class Fire_troll(Troll):
     hitpoints = 100
     mana = 50
     type = 'Fuego'
     atack = 20
     vulneravility = 'Agua'
class Earth_troll(Troll):
    hitpoints = 100
    mana = 50
    type = "Tierra"
    atack = 20
    vulneravility = 'Fuego'
class Air_troll(Troll):
    hitpoints = 100
    mana = 50
    type = 'Aire'
    atack = 20