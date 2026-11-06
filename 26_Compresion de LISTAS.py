numeros=[4,3,7,8,7,9,2,2,2,3]
#Dada esta lista de notas, crea otra lista
#Que contenga solo los aprobados ademas, le añadiras un punto extra a cada uno.
#Finalmente se imprime la lista
"""
lista2=[]

for i in numeros:
    if i>=5:
        lista2.append(i+1)
print(f"La lista de aprobados es {lista2}")

"""
#SE PUEDE HACER DE ESTA OTRA FORMA
#COMPRESION DE LISTAS
#lista=[operación for indice in lista (condición)]
lista2=[n+1 for n in numeros if n>=5]
print(lista2)

#convertir una lista en una tupla (datos estaticos, no se pueden modificar)

def obtener_aprobados():
    return tuple([n+1 for n in numeros if n>=5])

print(obtener_aprobados())

