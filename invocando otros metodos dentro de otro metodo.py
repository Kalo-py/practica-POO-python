class conClase():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro()

obj = conClase()
obj.metodo()
#El parámetro self también se usa para 
# invocar otros métodos desde dentro de la clase.
