import operaciones_bd as opbd
dni=input("Introduce el DNI: ")
nombre=input("Introduce el nombre: ")
email=input("Introduce el email: ")
curso=input("Introduce el curso: ")
nota=int(input("Introduce la nota: "))

opbd.alta_alumnos(dni,nombre,email,curso,nota)

    

