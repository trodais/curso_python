#LISTA DE REPRODUCCIÓN
#Se solicita la introducción de los datos de una nueva canción
#Si la canción no existe, se agrega a la lista. Si ya existe
#se agrega a la lista
#Después el programa muestra todos los títulos almacenados y la valoración
#media de toda la lista de reproducción
#CREO UNA FUNCION QUE ME DIGA SI LA CANCIoN EXISTE
"""
#UNA FORMA DE HACER LA FUNCION
def comprobar_cancion(titulo):
    
    for cancion in lista_reproduccion:
        if cancion["titulo"]==titulo;
            return True
    return False #Si llega aquí es porque no ha encontrado el título    """

#OTRA FORMA DE HACERLO
def comprobar_cancion(titulo):
    return titulo in [song["titulo"] for song in lista_reproduccion]

lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]   

txttitulo=(input("Introduce un titulo:"))
txtduracion=(float(input("Introduce una duración:")))
txtvaloracion=(int(input("Introduce su valoración: ")))
nueva_cancion={"titulo":txttitulo,"duracion":txtduracion,"valoracion":txtvaloracion}
#Comprueba si existe la canción
#Añade el nuevo diccionario a la lista de reproducción 
#Llamamo a la función comprobar_cancion definida arriba
if not comprobar_cancion(txttitulo): #SI NO DEVUELVE TRUE
        lista_reproduccion.append(nueva_cancion)
else:
    print(f"La canción no fue añadida porque esta repetida")
suma=0       
for c in lista_reproduccion:
    suma+=c["valoracion"]
    print(c["titulo"])
print(f"Valoracion media es: {suma/len(lista_reproduccion)}")


