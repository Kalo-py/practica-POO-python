class conClase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj = conClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._conClase__oculto()
#para acceder a una funcion/metodo oculto debemos escribir
#la clase y el metodo todo junto para poder invocar