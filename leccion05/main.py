# # Listas en python
# nombres = ['Juan', 'Karla', 'Ricardo', 'María']
# # Imprimir la lista de nombres
# print(nombres)
# # acceder a los elementos de manera individual
# # print(nombres[0])
# # print(nombres[1])
# # Acceder a los elementos de manera inversa
# # print(nombres[-1])
# # print(nombres[-2])

# # Listas parte 2
# # Imprimir un rango
# print(nombres[0:2]) #Sin incluir el índice 2
# # Ir del inicio de la lista al índice (sin incluirlo)
# print(nombres[ : 3])
# # Desde el índice indicado hasta el final
# print(nombres[1: ])
# # Cambiar valor
# nombres[3] = 'Ivonne'
# print(nombres)

# # Iterar lista
# for nombre in nombres:
#     print(nombre)
# # else: 
# #     print('No existen más nombres en la lista')

# # Preguntar el largo de una lista
# print(len(nombres))
# # Agregar un elemento (append)
# nombres.append('Alex')
# print(nombres)
# # Insertar un elemento en un índice en específico
# nombres.insert(1, 'Karina')
# print(nombres)
# # Remover un elemento
# nombres.remove('Juan')
# print(nombres)
# # Remover el último valor agregado
# nombres.pop()
# print(nombres)
# # Eliminar un elemento en un índice indicado
# del nombres[0]
# print(nombres)
# # Limpiar todos los elementos de la lista
# nombres.clear()
# print(nombres)
# # Borrar la lista por completo
# del nombres
# print(nombres)

# Tarea Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# for i in range(10):
#     if i % 3 == 0:
#         print(i)

# Tuplas. Ya no se pueden agregar, modificar ni eliminar elementos (inmutable)
# Si solo tiene un valor se debe de poner una coma al final
# frutas = ('naranja', 'plátano', 'guayaba')
# Largo de una tupla
# print(frutas[0])
# print(len(frutas))
# Acceder un rango de valores
# print(frutas[0:2])

# recorrer elementos

# for fruta in frutas:
#     print(fruta, end=' ')

# # cambiar el valor de una tupla
# # frutas[0] = 'Pera' No funciona
# frutasLista = list(frutas)
# frutasLista[0] = 'Pera'

# frutas = tuple(frutasLista)
# print('\n', frutas)

# # Eliminar la tupla
# del frutas

# Tarea Dada la siguiente dupla, crear una lista que sólo incluya los números menor que 5 utilizando el ciclo for
# tupla = (13, 1, 8, 3, 2, 5, 8)

# numerosLista = []

# for numero in tupla: 
#     if numero < 5:
#         numerosLista.append(numero)
        
# print(numerosLista)

# Set en python colección sin orden y sin indices
# planetas = {'Marte', 'Júpiter', 'Venus'}
# print(planetas)
# # largo
# print(len(planetas))
# # revisar si un elemento está presente
# print('Tierra' in planetas)
# # agregar elementos
# planetas.add('Tierra')
# print(planetas)
# # No soporta elementos duplicados
# planetas.add('Tierra')
# print(planetas)
# # eliminar elemento
# planetas.remove('Tierra')
# print(planetas)
# # Eliminar elemento sin arrojar error si no se encuentra el elemento
# planetas.discard('Júpiter')
# print(planetas)

# # Limpiar set
# planetas.clear()
# print(planetas)
# # eliminar el set
# del planetas

# Diccionarios (key, value)
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
# largo
print(len(diccionario))
# acceder a un elemento
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# modificar elemento
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)
# recorrer elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valores in diccionario.values():
    print(valores)

# comprobar si existe un elemento
print('IDE' in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario por completo
del diccionario