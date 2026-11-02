#¿Cual es la temperatura mas baja?
#UTILIZO LA COMPRESION DE LISTA, 1 convierto texto en lista de texto, despues comprimo para convertir
#en valores float y después calculo el mínimo
temperaturas="12.4,23.6,17.8,3.5,29.0,11.6"
temp=min([float(t) for t in temperaturas.split(",")])
print(temp)

    

