#Al iniciar el prorama se debe mostrar el siguiente menú:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota Media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo en acción. Después, vuelve a salir el menú
#y así hasta que elija la opción salir

#opc1=print("#1.- Añadir nota")
#opc2=print("#2.- Mostrar notas extremas")
#opc3=print("#3.- Total de aprobados")
#opc4=print("#4.- Nota Media")
#opc5=print("#5.- Mostrar todas")
#opc6=print("#6.- Salir")


opc_mostrar=0
notas=[]
aprobados=0

while opc_mostrar!=6:
    
    opc1=print("#1.- Añadir nota")
    opc2=print("#2.- Mostrar notas extremas")
    opc3=print("#3.- Total de aprobados")
    opc4=print("#4.- Nota Media")
    opc5=print("#5.- Mostrar todas")
    opc6=print("#6.- Salir")
    opc_mostrar=int(input("Introduce una opción del menú (1 al 6):"))
           
    match opc_mostrar:
        case 1:
                print(opc1)
                nota_in=input("Introduce la nota")
                notas.append(nota_in)
           
            
        case 2:
            print(f"Esta es la lista de notas ",notas) 
            print(f"La nota mayor es {max(notas)} y la nota menor es {min(notas)}")
            
        case 3:
            for n in notas:
                if n>5:
                    aprobados+=1
                    print("Los aprobados en este curso son: ",aprobados)

"""
notas=[]
opcion_elegida=0
while opcion_elegida!=6 :
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            notas.append(int(input("Introduce nota ")))
        case 2:
            print(f"nota más alta {max(notas)}")
            print(f"nota más baja {min(notas)}")
        case 3:
            aprobados=0
            for nota in notas:
                if nota>=5:
                    aprobados+=1
            print(f"total de aprobados {aprobados}")
        case 4:
            suma=0
            for nota in notas:
                suma+=nota
            if(len(notas)==0):
                print("No hay notas")
            else:
                print(f"nota media {suma/len(notas)}")
        case 5:
            print(notas)
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida") """