#Definiendo funciones
def hello():
    print("Hello World")

hello()

#Definiendo funciones con parametros
def saludo(nombre = ""):
    print("Hola " + nombre)

saludo("Santiago")

saludo()

#Funcion lambda
add = lambda numeroUno,numeroDos : numeroUno + numeroDos
print(add(5,3))
