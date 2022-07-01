class conClase:
    varia = 2
    def metodo(self):
        print(self.varia, self.var)

obj = conClase()
obj.var = 3
obj.metodo()

#El parámetro self es usado para obtener acceso 
# a la instancia del objeto y las variables de clase
