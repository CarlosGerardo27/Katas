# Ejercicio - Escribir declaraciones if, else, y elif

#Ejercicio 1

# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
velocidad_asteroide = 49 


if velocidad_asteroide > 25:# Escribe una expresión de prueba para calcular si necesita una advertencia.
    # Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
    print("PELIGRO INMINENTE: Se acerca un asteroide a más de " + str(velocidad_asteroide) + " Km/s")
else:
    print ("Todo tranquilo, la vida sigue")

#Ejercicio 2

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
velocidad_asteroide2 = 19

if velocidad_asteroide2 > 20:
    # Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
    print("Mirar hacia el cielo, es un pajaro, es un avión...nooo! es un astoreide!")
elif velocidad_asteroide2 == 20:
    print("Casi nos quedamos sin este espectaculo, pero miren hacia arriba que bonito que esta")
else:
    print("Esta vez no hay nada que ver")


# Ejercicio: Uso de operadores and y or
#Ejercicio 3

#condiciones
#Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros golpeara la Tierra, causaría mucho daño.
#La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.
#Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra.

tamaño_asteroide = 24
velocidad_asteroide3= 19 

if tamaño_asteroide > 25 or velocidad_asteroide3 > 25:
    print("Peligro inminente, un asteroide de " + str(tamaño_asteroide) + "metros se acerca a la tierra, resguardese")
elif velocidad_asteroide3 >= 20 and velocidad_asteroide3 < 25:
    print("Voltea al cielo, se puede ver la luz de un asteoroide")
elif velocidad_asteroide3 >= 20 and tamaño_asteroide < 25:
    print("Voltea al cielo, se puede ver la luz de un asteoroide")
else:
    print ("nada por aqui")


