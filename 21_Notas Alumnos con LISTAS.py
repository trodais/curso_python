notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
#Indica cuantos alumnos han aprobado
suma=0
for i in notas_alumnos:
    if i>=5:
        suma=suma+1
print(f"El número de alumnos que han aprobado es de {suma}")    
#DIME LA NOTA MAS ALTA
#FORMA 1
Nota_max=max(notas_alumnos)
print(f"Nota mas alta {Nota_max}")
#FORMA 2
mayor=notas_alumnos[0] #inicializamos la variable con el primer valor de la lista
for i in notas_alumnos:
    if i>mayor:
        mayor=i
print(f"La nota mayor es {mayor}")        
print(f"Las notas en orden son  {sorted(notas_alumnos,reverse=True)}")        
        
    
    