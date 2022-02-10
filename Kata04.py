text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Primero, divide el texto en cada oración para trabajar con su contenido:

texto_lowerCase = text.lower()

arreglo_texto = texto_lowerCase.split('.')
print(arreglo_texto)

## Define las palabras pista: average, temperature y distance suenan bien

pista = ["average", "temperature", "distance"]

print(pista)


#Cre un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
# Ciclo for para recorrer la cadena

for item in arreglo_texto:
    if item.find(str(pista)):
        print(item)

#Finalmente, actualiza el bucle(ciclo) para cambiar _C_ a _Celsius_:
# Ciclo para cambiar C a Celsius

text_celcuius = text.replace("C","Celcius")
print(text_celcuius)