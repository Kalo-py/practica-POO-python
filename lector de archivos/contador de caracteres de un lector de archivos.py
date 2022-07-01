from os import strerror

try:
    cnt = 0
    s = open('C:/Users/Carlos/Documents/programacion/python/hola.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1) #es el incrementador osea, va al siguiente caracter del archivo
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#Se usa el mecanismo try-except y se abre el archivo con el nombre (text.txt en este caso).
#Intenta leer el primer caracter del archivo (ch = s.read(1)).
#Si tienes éxito (esto se demuestra por el resultado positivo de la condición while), se muestra el caracter (nota el argumento end=,¡es importante! ¡No querrás saltar a una nueva línea después de cada caracter!).
#Se actualiza el contador (cnt).
#Intenta leer el siguiente carácter y el proceso se repite.