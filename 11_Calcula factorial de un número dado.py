#Realizar un programa que solicite la introducción de un nº y calcule su numero factoral 
multiplica=1
factorial=int(input("Introduce un nº que quieras calcular su factoria:   "))+1
for i in range(1,factorial):
    multiplica=multiplica*i
print(f"EL factorial de {factorial-1} es {multiplica}")


