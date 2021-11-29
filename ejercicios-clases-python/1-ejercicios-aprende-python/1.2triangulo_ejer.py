class Poligono:
    def __init__(self, color, lados, vertices = 0):
        self.vertices = vertices
        self.lados = lados
        self.color = color

class Triangulo (Poligono):
    def __init__(self, color, lados, vertices = 0):
        Poligono.__init__(self, color, lados, vertices = 0)
        self.vertices = vertices

#TIPOS DE TRIANGULOS: isoceles, equilatero, irregular

    def perimetro(self):
        perimetro = 0
        for lado in self.lados:
            perimetro += lado
        return perimetro
    
    def forma(self):
        lado1, lado2, lado3 = self.lados
        
        if lado1 == lado2 == lado3:
            return "EQUILATERO"

        elif lado1 == lado2:
            return "ISOCELES"
        
        elif lado1 == lado3:
            return "ISOCELES"

        elif lado2 == lado3:
            return "ISOCELES"
        
        else:
            return "IRREGULAR"

t1 = Triangulo ("rojo",[2, 5, 2])
print(f"Tu triangulo es un {t1.forma()} de color {t1.color} con {t1.perimetro()}m de perímetro.")

class Cuadrado(Poligono):
    def __init__(self, color, lados, vertices = 0):
        Poligono.__init__(self, color, lados, vertices = 0)
        self.vertices = vertices

    def perimetro(self):
        perimetro = 0
        for lado in self.lados:
            perimetro += lado
        return perimetro

c1 = Cuadrado("azul",[4, 4, 4, 4])
print(f"Tu cuadrado es de color {c1.color} con {c1.perimetro()}m de perímetro.")
