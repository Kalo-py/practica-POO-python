def printargs(args):
	lng = len(args)
	if lng == 0:
		print("")
	elif lng == 1:
		print(args[0])
	else:
		print(str(args))

try:
	raise Exception
except Exception as e:
	print(e, e.__str__(), sep=' : ' ,end=' : ')
	printargs(e.args)

try:
	raise Exception("mi excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

try:
	raise Exception("mi", "excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

#Hemos utilizado la función para imprimir el contenido de la propiedad args en tres casos diferentes, 
# donde la excepción de la clase Exception es lanzada de tres maneras distintas. Para hacerlo más espectacular, 
# también hemos impreso el objeto en sí, junto con el resultado de la invocación __str__().

#El primer caso parece de rutina, solo hay el nombre Exception despues de la palabra clave reservada raise. Esto significa que el objeto de esta clase se ha creado de la manera más rutinaria.

#El segundo y el tercer caso pueden parecer un poco extraños a primera vista, pero no hay nada extraño, son solo las invocaciones del constructor. 
# En la segunda sentencia raise, el constructor se invoca con un argumento, y en el tercero, con dos.

#Como puedes ver, la salida del programa refleja esto, mostrando los contenidos apropiados de la propiedad