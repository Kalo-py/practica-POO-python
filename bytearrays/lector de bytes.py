from os import strerror

try:
    bf = open('C:/Users/Carlos/Documents/programacion/python/hola.txt', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))