from os import strerror

try:
    ccnt = lcnt = 0
    s = open('C:/Users/Carlos/Documents/programacion/python/hola.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo: ", ccnt)
    print("Lineas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))

#Si no estás seguro de si el tamaño del archivo es lo suficientemente pequeño y no deseas probar el sistema operativo, puedes convencer 
# al método readlines() de leer no más de un número especificado de bytes a la vez (el valor de retorno sigue siendo el mismo, es una lista de una cadena).

#Siéntete libre de experimentar con este código de ejemplo para entender cómo funciona el método readlines().

#El tamaño máximo del búfer de entrada aceptado se pasa al método como argumento.

#Puedes esperar que readlines() procese el contenido del archivo de manera más efectiva que readline(), ya que puede ser invocado menos veces.