#pruebas creación de funciones

def suma():
    a=int(input("Introduce un número: "))
    b=int(input("Introduce otro número:"))
    suma=a+b
    print(f"La suma de {a} + {b} es ",suma)
    
def suma2():
    suma=a+b
    print(f"La suma de {a} + {b} es ",suma)    

def suma_n():
    a=int(input("¿Hasta que número entero quieres saber su suma?"))
    suma=0
    for i in range(1,a+1):
        suma+=i
    return print(f"La suma de numeros desde el 1 hasta el {a} es: {suma}")    

    
    
a=int(input("Introduce un número: "))
b=int(input("Introduce otro número:"))
suma2()
#suma_n()
#suma()
