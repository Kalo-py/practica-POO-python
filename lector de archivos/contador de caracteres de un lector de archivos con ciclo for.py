
from os import strerror

try:
    cnt = 0
    s = open('C:/Users/Carlos/Documents/programacion/python/hola.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#Abre el archivo, como anteriormente se hizo.
#Lee el contenido mediante una invocación de la función read().
#Despues, se procesa el texto, iterando con un bucle for su contenido, y se actualiza el valor del contador en cada vuelta del bucle.