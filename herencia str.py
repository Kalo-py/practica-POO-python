class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)
#Cuando Python necesita que alguna clase u objeto deba ser presentado como una cadena 
# (es recomendable colocar el objeto como argumento en la invocación de la función print()), 
# intenta invocar un método llamado __str__() del objeto y emplear la cadena que devuelve.