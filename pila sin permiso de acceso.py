class Pila:
    def __init__(self):
        self.__listaPila = []

objetoPila = Pila()
try:
    print(len(objetoPila.__listaPila))
except AttributeError:
    print("No tienes permisos")

#hacemos que la pila sea privada si ponemos una linea baja a la lista como por ejemplo __listaPila