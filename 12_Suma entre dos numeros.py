#Solicita la introducción de dos números y calcula la suma de todos los numeros comprendidos entre el menos y el mayor
suma = 0
num1=int(input("introduce el primer numero: "))
num2=int(input("introduce el segundo número:"))

if num1>num2:
    primero,segundo=(num2,num1)
else:
    primero=num1;segundo=num2    

for i in range(primero,segundo+1):
    suma=suma+i
print(f"La suma de {primero} con {segundo} es {suma} ")

"""
if num1>num2:
    primero,segundo=(num2,num1)
else:
    primero=num1;segundo=num2    

for i in range(primero,segundo+1):
    suma=suma+i
print(f"La suma de {primero} con {segundo} es {suma} ")"""