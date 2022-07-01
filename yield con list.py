def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = list(potenciasDe2(3))

print(t)
#La función list() puede transformar una serie de invocaciones de generador subsequentes en una lista real: