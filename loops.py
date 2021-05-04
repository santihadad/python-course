# Vamos a generar una lista con algunos alimentos
foods = ['manzanas', 'pan', 'queso', 'leche']
# print(foods[0])
# print(foods[1])
# print(foods[2])
# print(foods[3])

for food in foods:
    if food == "queso":
        print("Tienes que comprar esto")
        break
    print(food)

for food in foods:
    if food == "queso":
        print("Tienes que comprar esto")
        continue
    print(food)

#Utilizando el metodo range para imprimir valores
for number in range(1,11):
    print(number)

#Iterando Strings
for letter in "Hello":
    print(letter)

#Bucle While
count = 4
while count <= 10:
    print("Este valor es menor o igual a 4")
    count = count + 1
    print(count)