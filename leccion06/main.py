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

# def numeros(*args):
#     res = 1
#     for numbers in args:
#         res *= numbers
#     return res
        
# print(numeros(1, 3, 4))

# Argumentos variables llave - valor en python
# kwargs elementos con llave valor
# def listarTerminos(**terminos):
#     for llave, valor in terminos.items():
#         print(f'{llave}: {valor}')

# listarTerminos(IDE='Integrated Development Enviroment', PK = 'Primary Key')
# listarTerminos(DBMS = 'Database Management System')

# Distintos tipos de datos como argumentos en python
# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)

# nombres = ['Alejandro', 'Karina', 'Ceci', 'Victoria']
# desplegarNombres(nombres)
# desplegarNombres('Carlos')

# Funciones recursivas
# Es una función que se manda a llamar así misma para completar una tarea
# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         #Se quedan pendientes las llamadas en la memoria
#         return numero * factorial(numero-1) 

# resultado = factorial(5)
# print(f'El fatorial es {resultado}')

# Ejercicios
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas

# def imprimirNumeros (numero):
#     if numero >= 1:
#         print(numero)
#         imprimirNumeros(numero - 1)
        
# imprimirNumeros(int(input('Ingresa un número: ')))

# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# def calcImpuesto(valor, impuesto):
#     valorFinal = valor * (impuesto/100)
#     return round(valorFinal + valor, 2)

# valor = int(input('Ingresa el valor: '))
# impuesto = int(input('Ingresa el impuesto: '))

# print(calcImpuesto(valor, impuesto))

def celToFah(celsius):
    return round(celsius * (9/5) + 32, 2)

def fahToCel(fahrenheit):
    return round((fahrenheit - 32) * (5/9), 2)

celsius = float(input('Ingrese la temperatura en celsius: '))
fahrenheit = float(input('Ingrese la temperatura en fahrenheit: '))

print(f'La temperatura de celsius a fahrenheit es: {celToFah(celsius)}°F')
print(f'La temperatura de fahrenheit a celsius es: {fahToCel(fahrenheit)}°C')