class coche():
    largochasis=250
    anchochasis=120
    ruedas=4
    enmarcha=False
    def __init__(self):
        self.Pila=[250,120,4,False]

    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta varado"
micoche=coche()
print("El ancho de chasis es: ",micoche.anchochasis)
micoche.arrancar()
print(micoche.Pila)
print(micoche.estado())