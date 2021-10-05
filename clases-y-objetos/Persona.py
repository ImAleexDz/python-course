# Una clase es una plantilla donde se crean instancias y objetos
# Se recomienda que el nombre de las clases lleven mayúsculas
# pass indica que no tiene ningún contenido
# init método inicializador, permite agregar atributos e inicializarlos
# self: referencia al objeto que se va a agregar

# class Persona:
#     def __init__(self):
#         self.nombre = 'Alex'
#         self.apellido = 'Díaz'
#         self.edad = 27

# persona1 = Persona()
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

# Clase con argumentos
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Alejandro', 'Díaz', 27)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)