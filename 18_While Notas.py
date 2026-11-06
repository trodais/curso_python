#Solicita una nota, después otra y así sucesivamente hasta introducir
#un cero en un momento, no pedirá mas notas y mostrará la nota media de las introducidas hasta el momento

contador=0
nota_total=0
nota=1
while nota>0:
    
    nota_in=int(input("Introduce una nota: "))
    nota_total=nota_total+nota_in
    nota=nota_in
    contador=contador+1
    print(f"contador {contador} nota in {nota_in} nota_total {nota_total}" )    
    media=nota_total/contador
   

print(f"La nota media de {contador-1} valores es: {media} ")
    
    