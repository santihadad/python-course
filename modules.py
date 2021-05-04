# Importado el modulo datetime
import datetime
print(datetime.date.today())

print(datetime.timedelta(minutes=100))

#Otra forma de importar el timedelta
from datetime import timedelta
print(timedelta(minutes=60))

#Importando modulos creados por el usuario
import fmath
print(fmath.add(1, 2))

print(fmath.substract(1, 2))