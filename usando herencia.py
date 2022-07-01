class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()

for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
    for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, cls), end="\t")
    print()

#Python ofrece una función que es capaz de identificar 
# una relación 
# entre dos clases, y aunque su diagnóstico no es 
# complejo, puede verificar si una clase particular 
# es una subclase de cualquier otra clase
