#Solicitar la introducción de números, uno a uno
#y los guardamos en una lista. Después de pedir un número,
#pregunta si quiere introducir otros, si dice si(S), pide uno nuevo
#y así sucesivamente hasta que diga que no(N).
#Al final, muestra la lista completa.

lista1=[]
respuesta="s"
while respuesta=="s" or respuesta=='S':
    try:
        num_in=int(input("Introduce un número"))
        lista1.append(num_in)
        respuesta=input("¿Quieres seguir añadiendo números? s/n ")
    except ValueError:
        print("No es un valor númerico, vuelve a intentarlo")
print(f"Has acabado de introducir números en la lista {lista1}")    
  
  
