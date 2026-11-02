#asignacion de equipos
#Teniendo en cuenta que alevin es 10 años y benjamin es 16
#Hacer un programa que solicite la edad y nos muestre a que grupo pertenece
#pertenece (el mas cercano a su edad). La edad debe estar entre 9 y 18 años.
limite_inf,limite_sup,benjamin,alevin=9,18,10,16
edad=int(input("Introduce tu edad :"))
if edad<limite_inf or edad>limite_sup:
   print(f"POR TU EDAD NO PUEDES ESTAR NI EL EQUIPO DE ALEVINES NI BENJAMINES")
else:
    distancia_benjamin=edad-benjamin
    distancia_alevin=alevin-edad
    if distancia_benjamin<distancia_alevin:
        print("Eres Benjamin")
    else:
        print("Eres Alevin")
    
    

