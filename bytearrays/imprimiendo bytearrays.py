from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#Entonces, ¿cómo escribimos un arreglo de bytes en un archivo binario?

#Observa el código en el editor. Analicémoslo:

#Primero, inicializamos bytearray con valores a partir de 10; si deseas que el contenido del archivo sea claramente legible,
#  reemplaza el 10con algo como ord('a'), esto producirá bytes que contienen valores correspondientes a la parte alfabética del 
# código ASCII (no pienses que harás que el archivo sea un archivo de texto; sigue siendo binario, ya que se creó con un indicador - bandera wb).
#Después, creamos el archivo usando la función open(), la única diferencia en comparación con las variantes anteriores es que el modo de apertura contiene el indicador b.
#El método write() toma su argumento (bytearray) y lo envía (como un todo) al archivo.
#El stream se cierra de forma rutinaria.

#Analicémoslo:

#Primero, abrimos el archivo (el que se creó usando el código anterior) con el modo descrito como rb.
#Luego, leemos su contenido en el arreglo de bytes llamado data, con un tamaño de diez bytes.
#Finalmente, imprimimos el contenido del arreglo de bytes: ¿Son los mismos que esperabas?