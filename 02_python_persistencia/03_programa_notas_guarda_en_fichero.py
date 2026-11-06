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
#Las notas se guardan en un fichero

notas=[]
#CREAR FUNCIONES PROPIAS (Las funciones se tienen que crear antes de su uso)
def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
    
def nueva_nota():
    #Escribe en modo append en el fichero
    with open(dir_fichero, "a") as f: 
        f.write(nota_in+"\n") 
    #cierra el fichero automaticamente si abrimos con with    
    

def aprobados():
    with open(dir_fichero,"r") as f:
        nota=f.readline() 
        while nota!="": 
            if int(nota.strip())>=5:
                 aprobados+=1    
            nota=f.readline()         
    return aprobados 

def nota_maxima():
    with open(dir_fichero,"r") as f:
        notas=f.readlines() #ES TEXTO HAY QUE QUITARLE ADEMAS LOS SALTOS DE LINEA \n
    return max(notas,key=lambda n:float(n.strip()))

def nota_minima():
    with open(dir_fichero,"r") as f:
        notas=f.readlines() #ES TEXTO HAY QUE QUITARLE ADEMAS LOS SALTOS DE LINEA \n
    return min(notas,key=lambda n:float(n.strip()))


def media():
    
    suma=0
                
    with open(dir_fichero,"r") as f:
        notas=f.readlines() #ES TEXTO HAY QUE QUITARLE ADEMAS LOS SALTOS DE LINEA \n
        if(len(notas)==0):
            return 0        
        else:
            return sum(notas,key=lambda n:float(n.strip()))/len(notas)
        
def mostrar_notas():
    with open(dir_fichero,"r") as f:
        linea=f.readline()
        while linea!="":
            print(linea.strip())
            linea=f.readline() #hay que poner esta linea para que vuelva a leer

dir_fichero="notas.txt"
aprobados=0

while opc_mostrar!=6:
  
    menu()
    opc_mostrar=int(input("Introduce una opción del menú (1 al 6):"))
           
    match opc_mostrar:
        case 1:
           
            nueva_nota(input("Introduce la nota: ")
        case 2:
            """
            #Imprime todas las líneas del fichero 
            with open("notas.txt","r") as f: 
                notas=f.readlines() 
            notas_lista=(list(map(lambda n:float(n.strip()),notas)))
            print(f"Estas son todas las notas {notas_lista}")
            print(f"La nota mayor es {max(notas)} y la nota menor es {min(notas)}")
            print(f"Cuenta el numero de notas {len(notas_lista)}")
            """
            nota_maxima()
            
        case 3:
            
                    print(f"Los aprobados en este curso son: ",aprobados())
        case 4:
             media()
        case 5:
            mostrar_notas()  
            
"""
#PROGRAMA DEL PROFESOR

#Al iniciar el programa se debe mostrar el siguiente menú:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo ea acción. Despues, vuelve a salir el menú
#y así hasta que elija la opción de salir. 
#Las notas se guardan en un fichero
dir_fichero="notas.txt"
#funciones propias
def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")
def nueva_nota(nota):
    with open(dir_fichero,"a") as f:
        f.write(nota+"\n")
        
def aprobados():
    with open(dir_fichero,"r") as f:      
        aprobados=0
        linea=f.readline()
        while(linea!=""):
            if int(linea.strip())>=5:
                aprobados+=1
            linea=f.readline()
    return aprobados
def nota_baja():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return min(notas,key=lambda n:int(n.strip()))
def nota_alta():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    return max(notas,key=lambda n:int(n.strip()))
def media():
    with open(dir_fichero,"r") as f:
        notas=f.readlines()
    if not notas:
        return 0
    return sum([int(n.strip()) for n in notas])/len(notas)
def mostrar_notas():
    with open(dir_fichero,"r") as f:
        linea=f.readline()
        while linea!="":
            print(linea.strip())
            linea=f.readline()
#programa principal
#PARA TRATAR LAS EXCEPCIONES DE ERROR DE FICHEROS, LO ABRO EN MODO LECTURA Y SI NO EXISTE LO CREAMOS "ESCRITURA"mostrar_notas
try:
    f=open(dir_fichero,"r")
    f=.close()
except FileNotFoundError:
    f=open(dir_fichero,"r")
    f=.close()
opcion_elegida=0
while opcion_elegida!=6 :
    menu()
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            nueva_nota(input("Introduce nota "))
        case 2:
            print(f"nota más alta {nota_alta()}")
            print(f"nota más baja {nota_baja()}")
        case 3:
            print(f"total de aprobados {aprobados()}")
        case 4:
            print(f"La nota media es {media()}")
        case 5:
            mostrar_notas()
        case 6:
            print("Fin del programa!")
        case _:
            print("opción no válida") 




"""

            