#PRACTICA CON CONJUNTOS
#Los conjuntos no tienen orden
dia=input("Dime un día de la semana:")
dias={"lunes","martes","miercoles"}
#dias.remove("lunes")
if dia in dias:
    print("Ese dia ya existe")
else:
    dias.add(dia)    
print(dias)
lista_dias=list(dias)
print(lista_dias)

#convertir lista en conjuntos set

lista_numeros=[4,3,2,1,0,4,1,2,7,8,10,11,10]
conjunto_numeros=set(lista_numeros)
print(conjunto_numeros)