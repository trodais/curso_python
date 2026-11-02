"""
def sumatorio(x,y,z=0,w=0):
    return x+y+z+w

#Llamo a la función
print(sumatorio(6,5))
print(sumatorio(6,5,4))
print(sumatorio(6,5,4,9))
"""

#Esta función puede recibir cualquier valor desde 0 hasta n números
def sumatorio(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

print(sumatorio(4,1))    
print(sumatorio(4,1,10,13,12,15,16,27))   
print(sumatorio()) 


