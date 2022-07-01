def crearcierre(par):
	loc = par
	def potencia(p):
		return p ** loc
	return potencia

fsqr = crearcierre(2)
fcub = crearcierre(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))

#Esto significa que el cierre no solo utiliza el ambiente congelado, sino que también puede modificar su comportamiento utilizando valores tomados del exterior.

#Este ejemplo muestra una circunstancia más interesante: puedes crear tantos cierres como quieras usando el mismo código. Esto se hace con una función llamada crearcierre(). Nota:

#El primer cierre obtenido de crearcierre() define una herramienta que eleva al cuadrado su argumento.
#El segundo está diseñado para elevar el argumento al cubo.