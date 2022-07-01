
from os import strerror

try:
	fo = open('C:/Users/Carlos/Documents/programacion/python/hol.txt', 'wt') #un nuevo archivo (newtext.txt) es creado
	for i in range(10):
		a = str(input("Agrega algo papi: "))
		if a==str("stop"):
			break
		s=str(a+"\n")
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))

#El método se llama write() y espera solo un argumento: una cadena que se transferirá a un archivo abierto (no lo olvides), 
# el modo de apertura debe reflejar la forma en que se transfieren los datos - escribir en un archivo abierto en modo de lectura no tendrá éxito).

#No se agrega carácter de nueva línea al argumento de write(), por lo que debes agregarlo tu mismo si deseas que el archivo se complete con varias líneas.

#El ejemplo en el editor muestra un código muy simple que crea un archivo llamado newtext.txt (nota: el modo de 
# apertura w asegura que el archivo se creará desde cero, incluso si existe y contiene datos) y luego pone diez líneas en él.

#La cadena que se grabará consta de la palabra línea, seguida del número de línea. 
# Hemos decidido escribir el contenido de la cadena carácter por carácter (esto lo hace el bucle interno for) pero no estás obligado a hacerlo de esta manera.

#Solo queríamos mostrarte que write() puede operar con caracteres individuales.