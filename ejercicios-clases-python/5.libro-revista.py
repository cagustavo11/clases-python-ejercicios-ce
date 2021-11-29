"""
5. Escribe un programa para una biblioteca que contenga libros y revistas. Las características comunes que se almacenan tanto para las revistas como para los libros son el código, el título, y el año de publicación. Estas tres características se pasan por parámetro en el momento de crear los objetos.
Los libros tienen además un atributo prestado.
/ Los libros, cuando se crean, no están prestados.
/ Las revistas tienen un número. En el momento de crear.
En el momento de crear las revistas se pasa el número por parámetro.
/ Tanto las revistas como los libros deben tener (aparte de los constructores) un método que devuelve el valor de todos los atributos en una cadena de caracteres. También tienen un método que devuelve el año de publicación, y otro el código de libro o revista.
/ Se tiene que implementar métodos prestar(), devolver() y prestado().
//////////// Implementar una clase padre (superclase) de Libro y Revista con sus características comunes, que se llama Publicación.
En esta clase además de declarar los tres atributos, se implementa un constructor que reciba por parámetro el valor de los tres atributos, también se implementan un método que devuelve la información de estos tres atributos en forma de cadena.
/ Se implementan las clases Libro y Revista que añaden sus nuevos atributos.
/ Se escriben constructores, que llaman al constructor de la clase padre.
/ En las clases hija se sobrescribe el método que devuelve la información de los atributos (polimorfismo) para agregar el atributo especifico de la clase hija.
"""
import random


class Publicacion():

    def __init__(self, codigo, titulo, anio_publicacion):
        self.codigo = codigo
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
    # método que devuelve la informacion en forma de cadena

    def get_atributos(self):
        return f"Código: { self.codigo },\nTítulo: { self.titulo },\nAño de publicación: { self.anio_publicacion }"

    def get_anio_publicacion(self):
        return self.anio_publicacion

    def get_codigo(self):
        return self.codigo

    def get_titulo(self):
        return self.titulo


class Libro(Publicacion):
    prestado = False

    def __init__(self, codigo, titulo, anio_publicacion):
        Publicacion.__init__(self, codigo, titulo, anio_publicacion)

    def prestar(self):
        if self.prestado:
            return f"El libro {self.titulo} ya ha sido prestado."
        self.prestado = True
        return f"El libro {self.titulo} se te ha sido prestado con exito!"

    def devolver(self):
        self.prestado = False
        return f"El libro {self.titulo} se ha devuelto!"

    def estado_del_libro(self):
        if self.prestado == False:
            return "El libro NO esta en calidad de prestamo todavia"
        return "El libro YA está en calidad de prestamo"


class Revista(Publicacion):
    def __init__(self, codigo, titulo, anio_publicacion, numero):
        Publicacion.__init__(self, codigo, titulo, anio_publicacion)
        self.numero = numero


libros = [Libro(100, "Don Quijote de la Mancha", 1605)]


def encontrarLibro(libros, codigo, opcion):
    encontrado = False
    for libro in libros:
        if libro.codigo == codigo and opcion == 3:
            encontrado = True
            return libro.estado_del_libro()
        if libro.codigo == codigo and opcion == 2:
            encontrado = True
            return libro.devolver()
        if libro.codigo == codigo and opcion == 1:
            encontrado = True
            return libro.prestar()

    if not encontrado:
        return "El codigo del libro que usted ingreso no se encuentra"


def listar_codigos(libros):
    for libro in libros:
        print(
            f"Codigo del libro '{ libro.get_titulo() }': { libro.get_codigo() } ")


while True:
    # Menu de opciones
    opcion = int(input(
        "(1) Prestar un libro\n(2) Devolver Libro\n(3) Consultar estado de un libro\n(4) Listar Publicaciones\n(5) Agregar Publicación\n(6) Salir\nElige => "))
    if opcion == 1:
        # Listar el codigo de los Libros
        listar_codigos(libros)
        codigo = int(input("Ingrese el codigo del libro que sea prestarse: "))
        print(encontrarLibro(libros, codigo, opcion))

    elif opcion == 2:
        # Listar el codigo de los Libros
        listar_codigos(libros)
        codigo = int(input("Ingrese el codigo del libro que desea devolver: "))
        print(encontrarLibro(libros, codigo, opcion))

    elif opcion == 3:
        # Listar el codigo de los Libros
        listar_codigos(libros)
        codigo = int(
            input("Ingrese el codigo del libro que desea consular su estado: "))
        print(encontrarLibro(libros, codigo, opcion))

    elif opcion == 4:
        for libro in libros:
            print("-------------")
            print(f"{libro.get_atributos()}")
            print("-------------")

    elif opcion == 5:
        nombre = input("ingrese el nombre de la publicación: ")
        anio = int(input("ingrese el anio de la publicación: "))
        libros.append(Libro(100 + len(libros), nombre, anio))
    elif opcion == 6:
        break
