# Coche:
class Vehículo:
    kilometros_recorridos = 0
    
    def __init__(self, color, marca):

        self.color = color
        self.marca = marca

class Coche(Vehículo):
   #
    def __init__(self, color, marca, gasolina, matricula):
        Vehículo.__init__(self, color, marca)
        self.gasolina = gasolina
        self.matricula = matricula
        self.gasolina = gasolina

    def avanzar(self,km):
        self.kilometros_recorridos += km
        self.gasolina -= km*0.1

        if self.gasolina < 0:
            print("ES NECESARIO REPOSTAR PARA RECORRER LA CANTIDAD INDICADA DE KILOMETROS")
            self.gasolina += km*0.1
            coche.repostar()
        else:
            print(f"SU AUTO RECORRIÓ {self.kilometros_recorridos} KM")

            print(f"TE QUEDA {self.gasolina} LITROS DE GASOLINA, \n")

    def repostar(self, gasolina_litros):
        
        self.gasolina += gasolina_litros
        print (f"TIENES ACTUALMENTE {self.gasolina} LITROS DE GASOLINA")
    def get_marca(self):
        return self.marca
    def get_matricula(self):
        return self.matricula
    def get_gasolina(self):
        return self.gasolina
    def get_kilometros_recorridos(self):
        return self.kilometros_recorridos

# coche = Coche("Cele16-09", "HONDA", 60)
coche = Coche ("Blanco", "Audi", 60, "1122PKL"  )
gasolina_litros = int(input("INGRESE CUÁNTOS LITROS DE GASOLINA QUIERE LLENAR: "))
coche.repostar(gasolina_litros)
print('\n')
coche.avanzar(120)
print(f"Total de kms coche: {coche.kilometros_recorridos}. Gasolina: {coche.gasolina}")
coche.avanzar(40)
print(f"Total de kms coche: {coche.kilometros_recorridos}. Gasolina: {coche.gasolina}")

# Bicicleta
class Bicicleta(Vehículo):
    def __init__(self, color, marca, canasta):
        Vehículo.__init__(self, color, marca)

        self.canasta = canasta

    def avanzar(self, km):
        self.kilometros_recorridos += km
    def hinchar_ruedas(self):
        print("Es necesario hinchar la rueda para recorrer la cantidad indicada de kms")

bicicleta = Bicicleta("Negro", "BH", True)
bicicleta.avanzar(30)
print(f"Total de kms bici: {bicicleta.kilometros_recorridos}")
bicicleta.avanzar(25)
print(f"Total de kms bici: {bicicleta.kilometros_recorridos}")
bicicleta.hinchar_ruedas()
bicicleta.avanzar(25)
print(f"Total de kms bici: {bicicleta.kilometros_recorridos}")