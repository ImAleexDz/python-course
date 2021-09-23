# funciones
# Es un bloque de código que se puede ejecutar varias veces 
# def mi_funcion (nombre, apellido):
#     print(f'Nombre: {nombre}, Apellido: {apellido}')

# mi_funcion()

# Paso de argumentos
# mi_funcion('Alejandro', 'Díaz')

# Return
# def sumar(a, b):
#     return a + b

# resultado = sumar(5, 3)
# print(resultado)

# Valores por default en los parámetros de una función
# -> int especificar el tipo de dato
# def sumar(a = 0, b = 0):
#     return a + b

# resultado = sumar()
# print(resultado)

# Argumentos variables
# def listarNombres(*args):
#     for nombre in args:
#         print(nombre)

# listarNombres('Juan', 'Marcelo', 'Alejandro', 'Jessica')

# Ejercicio
# Crear una función para sumar los valores recibidos de tipo númerico, utilizando arumentos variables *args como parámetro de la función
# y regresar como resultado la suma de todos los valores pasados como argumetos

# Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la multiplicación de todos los valores pasados como argumentos.

def numeros(*args):
    res = 1
    for numbers in args:
        res *= numbers
    return res
        
print(numeros(1, 3, 4))