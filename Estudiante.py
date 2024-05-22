"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Enrique Mariño Jimñenez
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:
    """
    Clase persona con parámetros nombre, apellidos y nif.
    """
    def __init__(self, nombre, apellidos, nif):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nif = nif

    """
    Clase Persona con parámetrps apellidos, nombre y nif
    """


# noinspection PyRedeclaration
class Estudiante(Persona):
    """
    Clase Estudiante que hereda de Persona con parámetros nif, curso, nombre y apellidos)
    """
    def __init__(self, nif, curso, nombre, apellidos):
        super().__init__(nombre, apellidos, nif)
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self):
        """
        Propiedad que devuelve el nif.
        :return: Devuelve el valor de nif.
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Setter para definir el valor de nif.
        :param value: el nif que se introduzca.
        :return: devuelve el valor de value, que será el nif.
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Propiedad que devuelve el curso.
        :return: Devuelve el valor de curso.
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Setter para definir el valor de curso.
        :param value: el curso que se introduzca.
        :return: Devuelve el valor de value, que será el curso.
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Propiedad que devuelve el nombre.
        :return: Devuelve el valor de nombre.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Setter para definir el valor de nombre.
        :param value: el nombre que se introduzca.
        :return: Devuelve el valor de value, que será el nombre.
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Propiedad que devuelve los apellidos.
        :return: Devuelve el valor de apellidos.
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Setter para definir el valor de apellidos.
        :param value: los apellidos que se introduzcan.
        :return: Devuelve el valor de value, que serán los apellidos.
        """
        self.__apellidos = value
