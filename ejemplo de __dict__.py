class ClaseEjemplo:
    def __init__(self, val = 1):
        self.primera = val

    def setSegunda(self, val):
        self.segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.tercerita = 5

objetoEjemplo4 = ClaseEjemplo(5)
objetoEjemplo4.ultimaa = 6


print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)
print(objetoEjemplo4.__dict__)