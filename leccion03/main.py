# Sentencia if/else
# condicion = 'True'
# if condicion == True:
#     print('Condición verdadera')
# elif condicion == False:
#     print('Condición falsa')
# else:
#     print('Condición no reconocida')

# Modo debug (Paso a Paso) en sentencia if/else
# condicion = 10
# if condicion == True:
#     print('Condición verdadera')
# elif condicion == False:
#     print('Condición falsa')
# else:
#     print('Condición no reconocida')

# Ejercicio - Conversión de Número a Texto
# numero = int(input('Escribe un valor entre 1 y 3: '))
# numeroTexto = ''

# if numero == 1:
#     numeroTexto = 'Número uno'
# elif numero == 2:
#     numeroTexto = "Número dos"
# elif numero == 3:
#     numeroTexto = "Número tres"
# else: 
#     numeroTexto = "Valor fuera de rango"

# print(f'Número proporciondo: {numero}: {numeroTexto}')


# Sintaxis if else simplificada (Operador terniario)
# condicion = False

# print('Condicion verdadera') if condicion else print('Condicion falsa')

# Ejercicio - Calcular la estación según el mes proporcionado
# mes = int(input('Proporciona mes del año (1-12): '))
# estacion = None

# if mes == 1 or mes == 2 or mes == 12:
#     estacion = 'Invierno'
# elif mes == 3 or mes == 4 or mes == 5:
#     estacion = 'Primavera'
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = 'Verano'
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = 'Otoño'
# else:
#     estacion = 'Mes incorrecto'


# print(f'Para el mes {mes} la estación es: {estacion}')

# Ejercicio - Estapas de vida según edad
# edad = int(input('Proporciona tu edad: '))
# etapa = None

# if 0 <= edad < 10:
#     etapa = 'La infancia es increíble'
# elif 10 <= edad < 20:
#     etapa = 'Muchos cambios y mucho estudio'
# elif 20 <= edad < 30:
#     etapa = 'Amor y comienza el trabajo'
# else: 
#     etapa = 'Etapa de vida no reconocida'

# print(f'{edad} corresponde a la siguiente etapa de vida: {etapa}')

# Ejercicio - Sistema de calificaciones
calificacion = float(input('Proporciona un número entre 0 y 10: '))

if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion < 9:
    print('B')
elif 7 <= calificacion < 8:
    print('C')
elif 6 <= calificacion < 7:
    print('D')
elif 0 <= calificacion < 6:
    print('F')
else:
    print('Valor desconocido')