cursos="Java básico, Python principiantes, C, Java avanzado, Java EE, Python web, cobol"
#Solicitamos al usuario que introduzca un lenguaje que quiera aprender y le mostramos todos
#los cursos relacionados con ese lenguaje.

#Crear una lista a partir de la relación de cursos
lista_cursos=cursos.split(",")
lenguaje=input("Escribe el lenguaje de programación que quieres aprender")

for c in lista_cursos:
    if lenguaje.lower() in c.lower().split(" "): #Esto hace que la cadena de cada lenguaje lo divida a su vez en las palabras p.e Java EE
        print(c)