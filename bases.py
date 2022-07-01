class SuperUno:
    pass

class SuperDos:
    pass

class Sub(SuperUno, SuperDos):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)
#__bases__ es una tupla. La tupla contiene clases (no nombres de clases) que son superclases directas para la clase.
#Hemos definido una función llamada printBases(), diseñada para presentar claramente el contenido de la tupla.