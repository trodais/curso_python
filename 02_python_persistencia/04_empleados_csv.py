#Manejar ficheros CSV
import csv
"""
with open("empleados.csv",'r') as f:
    next(f) #Se ha saltado la primera fila
    datos=csv.reader(f,delimiter=",")
    for row in datos:
        print(row)
#Esto muestra el csv como un diccionario clave-valor         
with open("empleados.csv",'r') as f:
    datos=csv.DictReader(f,delimiter=",")
    for row in datos:
        print(row)

#Aplico la función list
with open("empleados.csv",'r') as f:
    datos=list(csv.reader(f,delimiter=","))
    for row in datos:
        print(row)
        
        
#Aplico list con DictReader NO se recorre el fichero al ser una lista
with open("empleados.csv",'r') as f:
    datos=list(csv.DictReader(f,delimiter=","))
print(row)
        
      
#Solicita la introducción de un departamento y te muestra los nombres de ese departamento
dep=input("Introduce el departamento: ")

with open("empleados.csv",'r') as f:
    datos=csv.DictReader(f)
    for emp in datos:
        if emp["departamento"]==dep:
            print(emp["empleado"])
""" 
#nombre con el empleado con mayor salario (UTILIZO UNA LISTA DE DICCIONARIOS DictReader)
with open("empleados.csv",'r') as f:
    datos=list(csv.DictReader(f))
    mayor_salario=max(datos,key=lambda n:n["salario"])
    print(f"El mayor salario es {mayor_salario["salario"]} corresponde al empleado {mayor_salario["empleado"]}")
    
            

        