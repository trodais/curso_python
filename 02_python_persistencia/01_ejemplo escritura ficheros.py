#me creo un archivo en modo "w" escritura
f=open("dias.txt","w")
f.write("lunes\n")
f.write("martes\n")
f.write("miercoles\n")
f.write("jueves\n")
f.write("viernes\n")
f.close()
print("Los dias se han guardado")