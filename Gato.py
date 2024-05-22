"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""

class Gato:

    def maullar(self):
        self.__miau = print('Miau')

    @property
    def miau(self):
        return self.__miau


g = Gato()
g.maullar()
