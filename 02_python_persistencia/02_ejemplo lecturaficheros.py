#EJEMPLO de lectura de ficheros 'r'
"""f=open("dias.txt",'r')
linea=f.readline()
while linea!="":
    print(linea)
    linea=f.readline()
f.close()    """

#Imprime todas las líneas del fichero 
with open("dias.txt","r") as f:
    linea=f.readline() 
    while linea!="": 
        print(linea) 
        linea=f.readline() 

#ahorramos el cierre
with open("dias.txt","r") as f:
    lista_dias=f.readlines()
print(lista_dias)    
#quita espacios y caracteres ocultos por la derecha e izquierda    
#    texto_limpio=texto.strip()


#lista_limpia=(list(map(lambda c:c.strip(),lista_dias))) otra forma de hacerlo
lista_limpia=[a.strip() for a in lista_dias]
print(lista_limpia)


