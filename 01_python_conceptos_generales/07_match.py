#LEE LA NOTA DE UN ALUMNO Y DEPENDIENDO DEL Nº (0 - 10) 
#SACA LA NOTA: SUSPENSO<5, APROBADO [5,6], NOTABLE [7,8], SOBRESALIENTE [9,10]
calificacion=int(input("INTRODUCE LA NOTA"))
match calificacion:
    case 1|2|3|4:
        print(f"TU NOTA ES {calificacion} HAS SACADO UN 'S U S P E N S O'")
    case 7|8:
        print(f"TU NOTA ES {calificacion} HAS SACADO UN 'N O T A B L E'" )       
    case 9|10:
        print(f"TU NOTA ES {calificacion} HAS SACADO UN 'S O B R E S A L I E N T E'" )      
    case _:
        print(f"TU NOTA ES INCORRECTA" )                       
            
            
