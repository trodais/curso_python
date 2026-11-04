#1-Nuevo libro
#2-Mostrar todos
#3-Buscar por titulo
#4-Libros por precio maximo
#5-Salir

"""
M I  C O D I G O


1- Se piden los datos del nuevo libro y se guardan
2- Se muestran los titulos de todos los libros
3- Se le pide el título y se muestran todos sus datos
4- Se le pide el precio máximo y se muestran los títulos de los libros cuyo precio sea igual o
   inferior
Después ejecutar cualquiera de los anteriores opcioens, se muestra de nuevo el menu.
Así hasta que elija la opción 5 que sale en el programa
   

#Creación de FUNCIONES para el programa
def menu():
    print("1.► Nuevo libro")
    print("2.► Mostrar todos los libros")
    print("3.► Buscar por título")
    print("4.► Listado de libros por precio máximo")
    print("5.► Salir")

def comprobar_libro(titulo):
    return titulo in [libro["titulo"] for libro in catalogo]

def titulos():
    print("Titulos de nuestro catalogo:")
    for lib for catalogo:
        print(f"Titulo: {lib["titulo"]} autor: {lib["autor"]}")



#PROGRAMA PRINCIPAL 
#catalogo=[{"titulo":"Don Quijote de la Mancha","autor":"M. Cervantes","editorial":"Cátedra","precio":20,"año":1987,"paginas":500}]
catalogo=[]
txtitulo=""
opcion_elegida=0
while opcion_elegida!=5 :
    #Llamo a la funcion menu() para que me lo muestre
    menu()
    opcion_elegida=int(input("Elige opción: "))
    match opcion_elegida:
        case 1:
            txtitulo=input("Introduce el título del libro: ")
            if not comprobar_libro(txtitulo): #SI NO DEVUELVE TRUE
                txautor=input("Introduce el autor: ")
                txeditorial=input("Introduce la editorial: ")
                txprecio=int(input("introduce el precio"))
                txanyo=int(input("Introduce el año del libro: "))
                txtpaginas=int(input("Introduce el número de páginas: "))
                nuevo_libro={"titulo":txtitulo,"autor":txautor,"editorial":txeditorial,"precio":txprecio,"año":txanyo,"paginas":txtpaginas}
                catalogo.append(nuevo_libro)
            else:
                print(f"El libro no fue añadido porque ya se encuentra en el catalogo")
        case 2:
            print(f"Estos son todos los libros de los que disponemos {catalogo}")        
        case 3:
            busca=input("introduce el titulo del libro que quieres ")
            if busca in [lib["titulo"] for lib in catalogo]:
                print("Tu libro si lo tenemos en nuestro catalogo")
"""                
"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
"""
libros=[]
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Nuevo libro")
    print("2 - Mostrar todos")
    print("3 - Buscar por título")
    print("4 - Libros por precio máximo")
    print("5 - Salir")
def titulos():
    print("Títulos de los libros:")
    for lib in libros:
        print(f"Título: {lib["titulo"]} precio:{lib["precio"]}")
def buscar_titulo(titulo):   
    encontrado=False    
    for i in libros:
        if titulo.lower() == i["titulo"].lower():
            print("Se ha encontrado tu libro")
            print(f"Título: {i['titulo']} Autor: {i['autor']} Precio: {i['precio']}")
            encontrado= True
            break
    if not encontrado:
        print("Libro no encontrado")
    return encontrado
def nuevo_libro():
	titulo = input("Título: ")
	autor = input("Autor: ")
	try:
		precio = float(input("Precio: "))
	except ValueError:
		print("Precio no válido. No se agregó el libro.")
		return
	if not buscar_titulo(titulo):
		libros.append({"titulo": titulo, "autor": autor, "precio": precio})
		print("Libro agregado.")
	else:
		print("Libro repetido, no se agregó")
def libros_por_precio_maximo(max_precio):  
    titulos = [n["titulo"] for n in libros if n["precio"]<=max_precio]    
    if len(titulos)>0:
        print(f"Libros con precio <= {max_precio}:")
        for j in titulos:
            print(j)  
    else:
        print("No hay libros con ese precio o inferior.")
opcion="0"    
while opcion!="5":
	mostrar_menu()
	opcion=input("Elige una opción: ")
	if opcion == "1":
		nuevo_libro()
	elif opcion == "2":
		titulos()
	elif opcion == "3":
		buscar=input("Introduce el titulo del libro que quieres buscar: ")
		buscar_titulo(buscar)
	elif opcion == "4":
		try:
			max_precio = float(input("Precio máximo: "))
			libros_por_precio_maximo(max_precio)
		except ValueError:
			print("Precio no válido.")
	elif opcion == "5":
		print("Saliendo del programa...")
	else:
		print("Opción no válida. Intenta de nuevo.") 

