# EJERCICIO DE CONDICIONALES, PIDE DOS NUMEROS Y MUESTRA EL RESULTADO DE DIVIDIR EL MAYOR ENTRE EL MENOR
num1=int(input("Introduce un número 1: "))
num2=int(input("Introduce un número 2: "))
if num1>num2:
    print(f"{num1} entre {num2} es {num1/num2}")
else:
    print(f"{num2} entre {num1} es {num2/num1}")
