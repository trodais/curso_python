#Realiza un programa que solicite la introducción de un número 
#después, muestra todos los pares entre 1 y ese número

num=int(input("Introduce un número: "))

for i in range(1,num+1):
    if num%2==0:
        print(i, "ES PAR")
