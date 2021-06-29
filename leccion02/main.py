# Operadores aritméticos
operandoA = 3
operandoB = 2
suma = operandoA + operandoB
# print('el resultado de la suma:', suma)
# F literal
# print(f'Resultado suma: {suma}')

# Resta
resta = operandoA - operandoB
# print(f'Resultado resta: {resta}')

# Multiplicacion
multiplicacion = operandoA * operandoB
# print(f'Resultado multiplicacion: {multiplicacion}')

# Division
division = operandoA / operandoB
# print(f'Resultado division: {division}')
division = operandoA // operandoB
# print(f'Resultado divisin (int): {division}')

# Módulo o residuo
modulo = operandoA % operandoB
# print(f'Resultado residuo división (módulo): {modulo}')

# Exponente
exponente = operandoA ** operandoB
# print(f'Resultado del exponente: {exponente}')

# Tarea
# alto = int(input('Proporciona el alto: '))
# ancho = int(input('Proporciona el ancho: '))
# area = alto * ancho
# perimetro = (alto + ancho) * 2
# print(f'El área del rectángulo es: {area}. El perímetro del rectángulo es: {perimetro}')

# Operadores de asignaión
# Asignación
miVariable = 10
# print(miVariable)

# Reasignación
miVariable = miVariable + 1
# print(miVariable)

# Incremento con reasignación
miVariable += 1
# print(miVariable)

# Decremento con reasignación
miVariable -= 2
# print(miVariable)

miVariable *= 3
# print(miVariable)

miVariable/= 2
# print(miVariable)

# operadores de comparación ***********
a = 4
b = 2

resultado = a == b
# print(f'Resultado ==: {resultado}')

resultado = a != b
# print(f'Resultado !=: {resultado}')

resultado = a > b 
# print(f'Resultado >: {resultado}')

resultado = a >= b
# print(f'Resultado >=: {resultado}')

resultado = a < b
# print(f'Resultado <: {resultado}')

resultado = a <= b
# print(f'Resultado <=: {resultado}')

# Algoritmo par o impar *******
# var_a = int(input('Escribe un valor numérico: '))

# if var_a % 2 == 0 :
#     print(f'El valor de {var_a} es un número par')
# else:
#     print(f'El valor de {var_a} es un número impar')

# Algoritmo si es mayor de edad ************
# edadAdulto = 18
# edad = int(input('Ingresa tu edad: '))

# if edad >= edadAdulto :
#     print('Eres mayor de edad')
# else :
#     print('Eres menor de edad')

# operadores lógicos and or y not ***********
# and. Devuelve true si ambos operandos son true
# or Devuelve true si alguno de los operandos es True
# not Devuelve true si alguno de los operandos son False

a = False
b = False
res = a and b
# print(res)

res = a or b
# print(res)

res = not a
# print(res)

# Ejercicio - Valor dentro de rango entre 0 y 5
# valor = int(input('Escribe el valor: '))
# valorMin = 0
# valorMax = 5

# dentroRango = (valor >= valorMin) and (valor <= valorMax)

# if dentroRango:
#     print(f'El valor {valor} está dentro de rango')
# else:
#     print(f'El valor {valor} está fuera de rango')

# Operador or preguntar si un padre puede asistir a ver el juego de su hijo (Si tiene vacaciones si puede asistir)
vacaciones = True
diaDescanso = False

# if vacaciones or diaDescanso:
#     print('Puede asistir al juego')
# else:
#     print('No puede asistir al juego')

# Operador not 

# if not (vacaciones or diaDescanso):
#     print('No puede asistir al juego')
# else:
#     print('Puede asistir al juego')

# ejercicio - Rango entre 20's y 30's
# edad = int(input('Ingresa tu edad: '))

# if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
#     print('Estás dentro del rango de los 20\'s o 30\'s')

#     if edad >= 20 and edad < 30:
#         print('Dentro de los 20\'s')
#     elif edad >= 30 and edad < 40:
#         print('Dentro de los 30\'s')
#     else: 
#         print('Fuera de rango')
        
# else:
#     print("No estás dentro de los 20's o los 30's")

# El mayor de dos números
# num1 = int(input('Proporciona el numero 1: '))
# num2 = int(input('Proporciona el numero 2: '))

# if num1 > num2:
#     print(f'El numero mayor es {num1}')
# elif num2 > num1:
#     print(f'El numero mayor es {num2}')
# else:
#     print('Los números son iguales')

# Ejercicio tienda de libros
print('Proporcione la siguiente información:')
name = input('Proporciona el nombre del libro: ')
idBook = int(input('Proporciona el ID: '))
price = float(input('Proporciona el precio: '))
isFree = input('Indica si el envío es gratuito (True/False): ')

if isFree == 'True':
    isFree = True
elif isFree == 'False':
    isFree = False
else:
    isFree = 'Valor incorrecto, debe escribir True o False'

print(f'''
    Nombre: {name}
    Id: {idBook}
    Precio: {price}
    Envío gratuito?: {isFree}
''')