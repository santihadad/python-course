#Los diccionarios nos sirven para relacionar una keyword con su valor, para no estar definiendo listas dentro de listas
#Definiendo un diccionario, con productos, cantidades y precio de referencia
product = {
    "name": "book",
    "quantity": 3, 
    "price": 4.99
}

person = {
    "first name": "Ryan",
    "last name": "Ray"
}

#Obtener los metodos de los diccionarios
print(dir(product))

#Obtener las keys dentro del diccionario "person" 
print(person.keys())

#Obtener las keys de cada diccionario con su respectivo elemento. Cada valor esta agrupado en una tupla, y todos los valores los coloca dentro de un arreglo
print(person.items())

#Limpiando los elementos dentro del diccionario. Al correr el codigo nos devuelve un "None"
print(person.clear())
