"""
Clase Gato.
:author: Enrique Mariño Jiménez.

"""


class Gato:
    """
    Clase gato con parámetro maulla
    """
    def __init__(self):
        self.maulla = print('Miau')

    def maullar(self):
        """
        Método que devuelve el valor de self.maulla.
        :return: Devuelve por pantalla 'Miau'.
        """
        return self.maulla


g = Gato()
g.maullar()
