import collections
import pprint

nombre_archivo='C:/Users/Carlos/Documents/programacion/python/hola.txt'
with open(nombre_archivo,"r") as f:
    conteo_caracteres=collections.Counter(f.read().lower())
    salida = pprint.pformat(conteo_caracteres)

print(conteo_caracteres)