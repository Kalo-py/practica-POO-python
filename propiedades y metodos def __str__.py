class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        Super.__init__(self, nombre)


obj = Sub("Andy")

print(obj)
#Como no existe el método __str__() dentro de la 
# clase Sub, la cadena a imprimir se producirá 
# dentro de la clase Super. Esto significa que el 
# método __str__() ha sido heredado por la clase Sub.
