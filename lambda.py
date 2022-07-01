def imprimirfuncion(args, fun):
	for x in args:
		print('f(', x,')=', fun(x), sep='')

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

#La función imprimirfuncion()se ha mantenido exactamente igual, pero no hay una función poli(). 
# Ya no la necesitamos, ya que el polinomio ahora está directamente dentro de la invocación de 
# la función imprimirfuncion() en forma de una lambda definida de la siguiente manera: lambda x: 2 * x**2 - 4 * x + 2

