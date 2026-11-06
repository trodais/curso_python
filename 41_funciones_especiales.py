import functools as ft
#Lista de números
numeros=[1,8,3,-4,9,-2,-11,16]
#lista con solo los positivos
positivos=list(filter(lambda n:n>0,numeros))
#positivos=[n for n in numeros n>0] otra forma de calcular los números positivos
pares=list(filter(lambda x:x%2==0,numeros))
print(positivos)
print(pares)

#calcula la suma de los cuadrados de todos los positivos
print(ft.reduce(lambda a,b:a+b,(map(lambda n:n**2,positivos))))

