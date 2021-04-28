demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colours = ['red', 'green', 'blue']
numbers = list((1, 2, 3, 4))

# print(numbers)
# print(type(numbers))

# numeros = list(range(1, 10))
# print(numeros)

# print(len(demo_list))

# Imprimir cierto valor pasando un indice
# print(demo_list[1])

# Imprimir indice inverso
# #print(demo_list[-2])

# Imprimir cierto elemento de una lista, si es que esta.
# print('green' in colours)
# print('negro' in colours) #Este valor no existe dentro de la lista

#Cambiar elementos de una lista
# print(colours)
# colours [1] = 'yellow'
# print(colours)

# Agregar un elemento a la lista con extend()
# colours.extend(['violet', 'yellow'])
# colours.extend(['pink', 'black'])
# print(colours)

# Agregar elemento en una posicion dada
# colours.insert(1, 'violet')
# colours.insert(len(colours), 'black')
# print(colours)

# Quitar elemento de la lista - este metodo solo remueve el ultimo elemento de la lista
# colours.pop()
# print(colours)

# Remover un elemento especifico de una lista
# colours.remove('red')
# print(colours)

# Eliminar todos los elementos de una lista
# colours.clear()
# print(colours)

# Ordenar los elementos
# print(colours)
# colours.sort()
# print(colours)
# colours.sort(reverse=True)
# print(colours)

# Obtener indice de un elemento
print(colours.index('blue'))
