ciudades={};
ciudades["Madrid"]=3200000
ciudades["Getafe"]=190000
ciudades["Alcorcón"]=120000
ciudades["Avila"]=70000
del(ciudades["Avila"])
#Recorre el diccionario por clave,valor
for k,v in ciudades.items():
    print(f"La ciudad {k} tiene {v} habitantes")

    