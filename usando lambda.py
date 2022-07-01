dos = lambda : 2
cuadrado = lambda x : x * x
potencia = lambda x, y : x ** y

for a in range(-2, 3):
    print(cuadrado(a), end=" ")
    print(potencia(a, dos()))

#La primer lambda es una función anónima sin parametros que siempre devuelve un 
# 2. Como se ha asignado a una variable llamada dos, podemos decir que la función ya no es anónima, y se puede usar su nombre para invocarla.

#La segunda es una función anónima de un parámetro que devuelve el valor de su argumento al cuadrado. Se ha nombrado también como tal.

#La tercer lambda toma dos parametros y devuelve el valor del primero elevado al segundo. El nombre de la variable que lleva la lambda habla por si mismo.