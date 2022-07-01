data = bytearray(11)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

#ytearrays se asemejan a listas en muchos aspectos. Por ejemplo, son mutables, son suceptibles a la función len(), 
# y puedes acceder a cualquiera de sus elementos usando indexación convencional.
#Existe una limitación importante - no debes establecer ningún 
# elemento del arreglo de bytes con un valor que no sea 
# un entero (violar esta regla causará una excepción TypeError) 
# y tampoco está permitido asignar un valor fuera del rango 
# de 0 a 255 (a menos que quieras provocar una excepción ValueError).
#Puedes tratar cualquier elemento del arreglo de bytes como 
# un valor entero - al igual que en el ejemplo en el editor.
