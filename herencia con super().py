class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        super().__init__(nombre)


obj = Sub("Andy")

print(obj)

#La función super() crea un contexto en el que no tiene que (además, no debe) pasar el argumento propio al método
# que se invoca; es por eso que es posible activar el constructor de la superclase utilizando solo un argumento.
#puedes usar este mecanismo no solo para invocar al constructor de la superclase, 
# pero también para obtener acceso a cualquiera de los recursos disponibles dentro de la superclase.

