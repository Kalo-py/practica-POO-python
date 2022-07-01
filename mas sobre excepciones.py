def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n

print(reciproco(2))
print(reciproco(0))






#Un código etiquetado de esta manera se ejecuta cuando (y solo cuando) 
# no se ha generado ninguna excepción dentro de la parte del try:. Podemos decir 
# que esta rama se ejecuta después del try: - ya sea el que comienza con except 
# (no olvides que puede haber más de una rama de este tipo) o la que comienza con else.)

#Nota: la rama else: debe ubicarse después de la última rama except.