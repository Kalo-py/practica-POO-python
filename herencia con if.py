
#herencia
class nom:
    def __init__(self, nombre):
        self.__nombre=nombre
    def __str__(self):
        return "hola mi nombre es "+self.__nombre+" un gusto"
class saludo(nom):
    def __init__(self, nombre):
        nom.__init__(self,nombre)



nombrecito=input("Agrega un nombre papu: ")
if nombrecito.isalpha():
    obj=saludo(nombrecito)
    print(obj)
else:
    print("vuelve a intentarlo")

