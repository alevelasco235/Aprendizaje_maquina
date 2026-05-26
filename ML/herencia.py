class Felino:
#En esta clase se define un constructor __init__ que recibe tres parámetros: nombre, color y edad. 
    def __init__(self, nombre, color, edad):
#En esta parte del código se asignan los valores de los parámetros a los atributos de la clase utilizando self.
        self.nombre = nombre

        self.color = color
        self.edad = edad
#En esta parte del código se define un método info que imprime la información del felino, incluyendo su nombre, color y edad.
    def info(self):
#En esta parte del código se imprimen los atributos del felino utilizando self para acceder a ellos.
        print("nombre", self.nombre)
        print("color", self.color)
        print("edad", self.edad)
        print("--------------")
#En esta parte del código se crean dos objetos de la clase Felino, gato1 y gato2, con diferentes valores para sus atributos. Luego se llama al método info para cada objeto para mostrar su información.
gato1=Felino("pelusa", "kalico", "3 años")
gato2=Felino("Mandarino", "naranja", "1 año")
print("--------------")
gato1.info()
gato2.info()
    