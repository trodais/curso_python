#FICHEROS JSON
import json
with open("alumnos.json",'r') as f:
    alumnos=json.load(f)  #los cargo todos en memoria
for a in alumnos:
    print(a["nombre"])    