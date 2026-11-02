#Hacer un programe que muestre la suma desde el 1 hasta el numero que introduzcamos
suma=0
limite=int(input("Introduce un número mayor de 1"))+1
for i in range(1,limite):
          suma=suma+i
print(f"la suma de {i} su suma es {suma}")