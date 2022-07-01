class ClaseEjemplo:
    attr = 1

print(hasattr(ClaseEjemplo, 'attr'))
print(hasattr(ClaseEjemplo, 'prop'))

#No olvides que la función hasattr() también puede operar en clases. 
# Puedes usarlo para averiguar si una variable de clase está disponible, como en el ejemplo en el editor
