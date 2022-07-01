def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)

#Hemos puesto yield en lugar de return. Esta pequeña enmienda convierte la función en un generador, y el ejecutar la sentencia yield tiene algunos efectos muy interesantes.

#Primeramente, proporciona el valor de la expresión especificada después de la palabra clave reservada yield, al igual que return, pero no pierde el estado de la función.

#Todos los valores de las variables están congelados y esperan la próxima invocación, cuando se reanuda la ejecución (no desde cero, como ocurre después de un return).

#Hay una limitación importante: dicha función no debe invocarse explícitamente ya que no es una función; es un objeto generador.
#
#