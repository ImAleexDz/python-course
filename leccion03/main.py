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
numero = int(input('Escribe un valor entre 1 y 3: '))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = "Número dos"
elif numero == 3:
    numeroTexto = "Número tres"
else: 
    numeroTexto = "Valor fuera de rango"

print(f'Número proporciondo: {numero}: {numeroTexto}')


