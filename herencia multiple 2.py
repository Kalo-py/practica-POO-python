class Derecha:
    var = "D"
    varDerecha = "DD"
    def fun(self):
        return "Derecha"


class Izquierda:
    var = "I"
    varIzquierda = "II"
    def fun(self):
        return "Izquierda"

class Sub(Izquierda, Derecha):
    pass


obj = Sub()

print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())
#Dentro del objeto mismo.
#En sus superclases, de abajo hacia arriba.
#Si hay más de una clase en una ruta de herencia, Python las escanea de izquierda a derecha.