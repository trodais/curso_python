cursos=["Java básico", "Python principiantes", "C","C#","C++","Java avanzado", "Java EE", "Python web", "cobol", "Fortran", "Visual Basic"]
#Solicitamos al usuario que introduzca un lenguaje que quiera aprender y le mostramos todos
#los cursos relacionados con ese lenguaje.


#PREGUNTA AL USUARIO QUE LENGUAJE QUIERE APRENDER
#EL PROGRAMA LE INDICARA SI EXISTE UN CURSO PARA ELLO O NO
lenguaje=input("Escribe el lenguaje de programación que quieres aprender:  ")

#EL in sirve para comparar el valor con todos los valores de la lista
#Comprimir la lista [c.lower() for c in cursos] (la lista es cursos)
"""if lenguaje.lower() in [c.lower() for c in cursos]:
    print("Tengo ese curso")
else: 
    print("No tengo ese curso")    
    """
cadena=lenguaje[:5]    

if lenguaje.lower() in [c.lower() for c in cursos]:
    print(cursos)


    