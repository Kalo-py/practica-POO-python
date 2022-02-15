class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  
    def getlista(self):
        return self.__listaPila

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0


    def getSuma(self):
        return self.__sum
    
    def getlista(self):
        return super().getlista()
    

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val


objetoPila = SumarPila()
print(objetoPila.__dict__)
#creamos la lista
for i in range(5):
    objetoPila.push(i)
print("La suma total es: ", objetoPila.getSuma())
print(objetoPila.getlista())
print(objetoPila.__dict__)
#eliminamos elementos de la lista ya creada
for i in range(5):
    print(objetoPila.pop(),end=",")
