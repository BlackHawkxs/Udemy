class Troll:
    hitpoints = 100
    mana = 50
    element = 'Common'
    atack = 20
    vulneravility = 'Ninguna'

    def __str__(self):
        return 'El trol de {} tiene {} puntos de vida y {} de mana, tiene {} puntos de ataque y es vulnerable a los ataque de tipo {}'.format(
            self.element, self.hitpoints, self.mana, self.atack,
            self.vulneravility)

    


class Ice_troll(Troll):
    hitpoints = 100
    mana = 50
    element = 'Agua'
    atack = 20
    vulneravility = 'Tierra'

    #def __str__(self):
     # return "Estas luchando contra el trol de {}".format(self.element)


class Fire_troll(Troll):
    hitpoints = 100
    mana = 50
    element = 'Fuego'
    atack = 20
    vulneravility = 'Agua'


class Earth_troll(Troll):
    hitpoints = 100
    mana = 50
    element = "Tierra"
    atack = 20
    vulneravility = 'Fuego'


class Air_troll(Troll):
    hitpoints = 100
    mana = 50
    element = 'Aire'
    atack = 20
