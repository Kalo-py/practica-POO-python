import time

class Vehiculo:
    def cambiardireccion(izquierda, on):
        pass

    def girar(izquierda):
        cambiardireccion(izquierda, True)
        time.sleep(0.25)
        cambiardireccion(izquierda, False)

class VehiculoOruga(Vehiculo):
    def control_de_pista(izquierda, alto):
        pass

    def cambiardireccion(izquierda, on):
        control_de_pista(izquierda, on)

class VehiculoTerrestre(Vehiculo):
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def cambiardireccion(izquierda, on):
        girar_ruedas_delanteras(izquierda, on)

#La ventaja más importante (omitiendo los problemas de legibilidad) es que esta forma de código te permite implementar un nuevo algoritmo 
# de giro simplemente modificando el método girar(), lo cual se puede hacer en un solo lugar, ya que todos los vehículos lo obedecerán.

#Así es como el el polimorfismo ayuda al desarrollador a mantener el código limpio y consistente.






