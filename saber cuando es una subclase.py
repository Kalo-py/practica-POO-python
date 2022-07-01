class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(cls1, cls2), end="\t")
    print()

#Python ofrece una función que es capaz de identificar 
# una relación 
# entre dos clases, y aunque su diagnóstico no es 
# complejo, puede verificar si una clase particular 
# es una subclase de cualquier otra clase
