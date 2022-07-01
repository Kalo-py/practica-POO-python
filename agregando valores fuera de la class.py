class conClase:
    def __init__(self, valor = None):
        self.var = valor

name=str(input("Agrega una cadena papi: "))
obj1 = conClase(name)
obj2 = conClase()

print(obj1.var)
print(obj2.var)
#agregamos un valor fuera de la clase
