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


notas=[]
#CREAR FUNCIONES PROPIAS (Las funciones se tienen que crear antes de su uso)
def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")

def aprobados():
    aprobados=0
    for nota in notas:
        if nota>=5:
            aprobados+=1
    return aprobados 
def media():
        suma=0
        for nota in notas:
            suma+=nota
        if(len(notas)==0):
            return 0
        else:
            return suma/len(notas)

#PROGRAMA PRINCIPAL
opcion_elegida=0
while opcion_elegida!=6 :
    #Llamo a la funcion menu() para que me lo muestre
    menu()
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            notas.append(int(input("Introduce nota ")))
        case 2:
            print(f"nota más alta {max(notas)}")
            print(f"nota más baja {min(notas)}")
        case 3:
            
            print(f"total de aprobados {aprobados()}")
        case 4:
            print(f"La nota media es {media()}")
        case 5:
            print(notas)
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida") 