lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()

#La función map() aplica la función pasada por su primer argumento a todos los elementos de
#  su segundo argumento y devuelve un iterador que entrega todos los resultados de funciones 
# posteriores. Puedes usar el iterador resultante en un bucle o convertirlo en una lista usando la función list().

#explicacion
#Se construye la lista1 con valores del 0 al 4.
#Después, se utiliza map junto con la primer lambda para crear una nueva lista en la que 
# todos los elementos han sido evaluados como 2 elevado a la potencia tomada del elemento correspondiente de lista1.
#lista2 es entonces impresa.
#En el siguiente paso, se usa nuevamente la función map() para hacer uso del generador que devuelve, 
# e imprimir directamente todos los valores que entrega; como puedes ver, hemos usado el segundo lambda aquí - solo eleva al cuadrado cada elemento de lista2.

