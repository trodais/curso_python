#ordenar listas
lista=[5,2,11,6,44,20,1]
lista_ordenada=sorted(lista,reverse=True)
otra_lista=set(lista)
#reversed=True ordena de mayor a menor
print(lista_ordenada)
print(f"Otra lista", otra_lista)
nombres=["bicicleta","oro","casa","martillo"]
print(sorted(nombres))

#ordenación personalizada, por ejemplo por el número de caracteres
print(sorted(nombres,key=lambda e:len(e)))

#De la lista de numeros, imprime el mayor de la lista
print(max(lista))

#imprimir el menor de la lista de nombres
print(min(nombres))

#imprime el que tiene menos caracteres
print(min(nombres,key=lambda n:len(n)))

