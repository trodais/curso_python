#LISTAS
#muestra los números pares de la lista
lista=[1,5,6,2,3,5,2,10]
"""
for n in lista:
    if n%2==0:
        print(n) """
#sustituye cada elemento de la lista por su cuadrado y luego imprimes la lista entera 
#y la suma de todo su contenido
"""
suma=0
indice=0
#print(len(lista))
for i in lista:
    lista[indice]=i**2
    indice=indice+1
  
print(lista)    
for num in lista:
    suma=suma+num
print(f"La suma de los datos de la lista {lista} es {suma}")    
"""

#SOLUCION ALTERNATIVA
#enumerate(lista) lo que hace es darte dos parametros el indice y el valor
for indice,num in enumerate(lista):
    lista[indice]=num**2
print(lista)    
suma=0
for num in lista:
    suma=suma+num
print(f"La suma de los datos de la lista {lista} es {suma}")    