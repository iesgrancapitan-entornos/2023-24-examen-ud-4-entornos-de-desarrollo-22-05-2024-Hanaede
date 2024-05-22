"""
Clase Gato.
:author: Enrique Mariño Jiménez.

"""


class Gato:

    def __init__(self):
        self.maulla = print('Miau')

    def maullar(self):
        return self.maulla


g = Gato()
g.maullar()
