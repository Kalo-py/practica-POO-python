import time

class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)

class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)

conRuedas = Vehiculo(Ruedas())
conPistas = Vehiculo(Pistas())

conRuedas.girar(True)
conPistas.girar(False)

#La composición es el proceso de componer un objeto usando otros objetos diferentes.
#  Los objetos utilizados en la composición entregan un conjunto de rasgos deseados 
# (propiedades y / o métodos), podemos decir que actúan como bloques utilizados para construir una estructura más complicada.