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
for i in range(10):
    if i % 3 == 0:
        print(i)