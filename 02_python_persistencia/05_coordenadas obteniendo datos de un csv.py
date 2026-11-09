#EJERCICIO 28 (las coordenadas estan en un fichero csv)
import math,csv

""" Se pide al usuario su posición, después el programa
le mostrará las coordenadas del punto 
más cercano a su posición """
import math
import csv

def distancia(punto1,punto2):
   return math.dist(punto1,punto2)
   return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1]) 

pos_usuario=(int(input("Tu posición x: ")),int(input("Tu posición y: ")))
dir_fichero="coordenadas.csv"

"""
#S O L U C I O N   C L A S I C A
#En esta variable se obtendrá la distancia más corta
distancia_corta=None
#En esta variable se deberá obtener la tupla de la tienda más cercana
coordenada_tienda=None
with open(dir_fichero,"r") as f:
    coordenadas=csv.DictReader(f)
    for row in coordenadas:
        coord=(int(row["x"]),int(row["y"]))
        if distancia_corta==None: #es la primera vez
            distancia_corta=distancia(coord,pos_usuario)
        if coordenada_tienda==None:
            coordenada_tienda=coord
        #recorremos las coordenadas y para cada una de ellas,
        #obtenemos la distancia con la posición del usuario. Si encontramos que esa distancia
        #es inferior distancia_corta, actualizamos tanto las variables distancia_corta
        #como coordenada_tienda
        dist=distancia(coord,pos_usuario)
        if dist<distancia_corta:
            distancia_corta,coordenada_tienda=dist,coord
print(f"La tienda mas cercana a {pos_usuario} tiene de coordenadas {coordenada_tienda}") 

"""
#Esta sería la forma reducida
with open(dir_fichero,"r") as f:
    coordenadas=list(csv.DictReader(f))
    distancia_corta=min(coordenadas,key=lambda c:(distancia((int(c["x"]),int(c["y"])),pos_usuario)))
    print(f"La tienda mas cercana es ",distancia_corta)                        
    #Con min estamos sacando la distancia minima (se recorre todas y la meto dentro de la función distancia)