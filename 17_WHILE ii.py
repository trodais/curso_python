#Se solicita la inserción de un número y el programa nos dirá
#si es par o impar. Después, se pregunta si quiere introducir otro número
#Si dice que sí(S), se vuelve a pedir el número y a indicar si es par o impar. 
#A continuación se vuelve a preguntar si quiere introducir otro número, y así hasta
#que diga que no(N) 


verifica="s"

while verifica=="s" or verifica=="S":
    num=int(input("Introduce un número: "))
    if num%2==0:
        print({num}, "ES PAR")
    else:
        print({num},"ES IMPAR")
    verifica=(input("¿Quieres introducir otro número? Contestar s/n:   "))
    print("EL PROGRAMA HA TERMINADO")
    
