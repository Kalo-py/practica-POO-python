class conClase:
    pass

print(conClase.__name__)
obj = conClase()
print(type(obj).__name__)
#La propiedad contiene el nombre de la clase. No es nada emocionante, es solo una cadena.
#i deseas encontrar la clase de un objeto en particular, puedes 
# usar una función llamada type(), la cual es capaz (entre otras cosas) de encontrar
#  una clase que se haya utilizado para crear instancias de cualquier objeto.