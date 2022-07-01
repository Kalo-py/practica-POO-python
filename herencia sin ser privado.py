# Probando propiedades: variables de instancia
class Super:
    def __init__(self):
        self.hola = 11

class Sub(Super):
    def __init__(self):
        Super.__init__(self)
        self.subVar = 12

obj = Sub()

print(obj.subVar)
print(obj.hola)

