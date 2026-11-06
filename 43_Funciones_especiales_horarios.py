cursos=[
    {"denominacion":"Python y datos","horario":"mañana","fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","horario":"mañana","fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","horario":"tarde","fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","horario":"festivos","fecha_fin":"30/09/2025"}  
] 

#Se pide al usuario que introduzca horario y le mostraremos
#los nombrre sde los cursos con ese horario
elec_horario=input("introduce el horario:")
#curso=list(map(lambda lib:lib["denominacion"],filter(lambda c:c["horario"]==elec_horario,cursos)))
curso=list(map(lambda l:l["denominacion"],
               filter(lambda c:c["horario"]==elec_horario,cursos))) 
print(curso)


