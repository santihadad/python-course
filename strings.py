myStr = "Hello World"

print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'Bye').upper())
print(myStr.count('l'))
print(myStr.startswith('Hola'))

print(myStr.split('o'))
print(myStr.find('o'))

print(len(myStr))

print(myStr.index('e'))

print(myStr.isalpha())
print(myStr.isnumeric())

print(myStr[4])
print(myStr[2])
print(myStr[5])
print(myStr[-2])

#CONCATENAR STRINGS

print("Hola este es el primer " + myStr)
print(f"Hola este es el primer {myStr}")
print("Hola este es el primer {0}".format(myStr))