cursos=["Java","Python","Typescript","C","Dart"]
#PREGUNTA AL USUARIO QUE LENGUAJE QUIERE APRENDER
#EL PROGRAMA LE INDICARA SI EXISTE UN CURSO PARA ELLO O NO
lenguaje=input("Escribe el lenguaje de programación que quieres aprender")
"""
# variable.upper() (todo en mayusculas) variable.lower() (todo minusculas)
encontrado=False
for i in cursos:
    if i.lower()==lenguaje.lower():
        print(f"El programa que has elegido es {i}") 
        encontrado=True
        break   
if not encontrado:
    print("Este programa no lo tenemos en nuestro programa")  
"""

#EL in sirve para comparar el valor con todos los valores de la lista
#Comprimir la lista [c.lower() for c in cursos] (la lista es cursos)
if lenguaje.lower() in [c.lower() for c in cursos]:
    print("Tengo ese curso")
else: 
    print("No tengo ese curso")    