class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)
    
    def geti(self):
        print("el contenido total de la lista")
        return self.__listaPila
        

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  



class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0
        

    def getSuma(self):
        return self.__sum

    def get(self):
        va=Pila.geti(self)
        return va
    

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)



    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val


objetoPila = SumarPila()
#creamos la lista
for i in range(5):
    objetoPila.push(i)

print("La suma total es: ", objetoPila.getSuma())
print(objetoPila.get())
#podemos invocar una variable privada de dos formas, creando un metodo que te devuelva ese valor o lo de abajo
print(objetoPila._Pila__listaPila)
#para imprimir una variable de una lista heredada
#debes poner el nombre de tu objeto definido en este caso "objetoPila" y seguidamente poner
#el nombre del objeto en donde se encuentra tu variable privada
#luego poner la variable privada
for i in range(5):
    print(objetoPila.pop(),end=",")

#eliminamos elementos de la lista ya creada