#Solicita la introducción de una contraseña, si es correcta
#le dice es un usuario válido. Si no es correcta, se le vuelve a pedir, 
#Así, hasta tres intentos. Si después del tercer intento la contraseña
#le dice que no es un usuario válido.

intentos=3
acertados=False
pwd_ok="hola"

while intentos>0 and acertado==False:
    pwd=input("Introduce la contraseña")
    if pwd_ok==pwd:
        acertados=True
    else:    
       print("Vuelve a intentar") 
       intentos=intentos-1
if acertado==True:       
    print(f"Tu contraseña ES correcta")
else:
print("TU CONTRASEÑA NO ES CORRECTA")   
    
        
