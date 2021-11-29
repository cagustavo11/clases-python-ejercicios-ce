#Crea las clases Persona, Cliente y Vendedor,
#identifica la relación de herencia e implementa
#la creación dos Vendedores: Vendedor de turno
#día y Vendedor de turno noche.

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_edad(self):
        return self.edad
    def get_dinero(self):
        return self.dinero

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, dinero):
        Persona.__init__(self, nombre, apellido, edad)
        self.dinero = dinero

    def comprar(self):
        return "misio"
        
class Vendedor(Cliente):
    def __init__(self, nombre, apellido, edad, dinero, negocio):
        Persona.__init__(self, nombre, apellido, edad)
        self.dinero = dinero
        self.negocio = negocio

    def vender(self):
        return "rico"
        
    def get_negocio(self):
        return self.negocio
 
class Vendedor_día(Vendedor):
    def __init__(self, nombre, apellido, edad, dinero, negocio):
        Vendedor.__init__(self, nombre, apellido, edad, dinero, negocio)
        self.negocio = negocio

class Vendedor_noche(Vendedor):
    def __init__(self, nombre, apellido, edad, dinero, negocio):
        Vendedor.__init__(self, nombre, apellido, edad, dinero, negocio)
        self.negocio = negocio

persona1 = Persona("Lee Min", "Ho", 34)
persona2 = Vendedor("Juanito", "Pérez", 35, 300, "Los pollitos de Juanito")
persona3 = Vendedor_día("Lucas", "Morales", 26, 400, "Delicias helada")
persona4 = Vendedor_noche("Carlitos", "Sánchez", 25, 350,"Salchipapas Carlito's")

print ()
print (f"La persona relacionada en todo es {persona1.get_nombre()} {persona1.get_apellido()} de {persona1.get_edad()} años")
print (f"El vendedor general es {persona2.get_nombre()} {persona2.get_apellido()} de {persona2.get_edad()} años, y gana al día {persona2.get_dinero()} soles, su negocio se llama {persona2.get_negocio()}")
print ()
print (f"****Vendedor de día****")
print (f"{persona3.get_nombre()} {persona3.get_apellido()} de {persona3.get_edad()} años")
print (f"Al día gana {persona3.get_dinero()} soles")
print (f"Su negocio se llama {persona3.get_negocio()} \n")

print (f"****Vendedor de noche****")
print (f"{persona4.get_nombre()} {persona4.get_apellido()} de {persona4.get_edad()} años")
print (f"Al día gana {persona4.get_dinero()} soles")
print (f"Su negocio se llama {persona4.get_negocio()}")