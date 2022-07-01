def exterior(par):
	loc = par
	def interior():
		return loc
	return interior

var = 1
fun = exterior(var)
print(fun())

#La función interior() devuelve el valor de la variable accesible dentro de su alcance, ya que interior() puede utilizar cualquiera de las entidades a disposición de exterior().
#La función exterior() devuelve la función interior() por si misma; mejor dicho, devuelve una copia de la función interior() al momento de la invocación de la función exterior(); 
# la función congelada contiene su entorno completo, incluido el estado de todas las variables locales, lo que también significa que el valor de loc se retiene con éxito, aunque exterior() 
# ya ha dejado de existir.
#En efecto, el código es totalmente válido y genera: