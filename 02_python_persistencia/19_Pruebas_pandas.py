import pandas as pd
lista_reproduccion=[{
  "_id": {
    "$oid": "6af5e1701b4958cb8bfc80f9"
  },
  "empleado": "Juan",
  "edad": 35,
  "salario": 1200,
  "departamento": "ventas"
},{
  "_id": {
    "$oid": "6af5e1701b4958cb8bfc80fa"
  },
  "empleado": "Marcos",
  "edad": 39,
  "salario": 1300,
  "departamento": "informática"
},{
  "_id": {
    "$oid": "6af5e1701b4958cb8bfc80fb"
  },
  "empleado": "Raquel",
  "edad": 28,
  "salario": 1100,
  "departamento": "ventas"
}]
#df=pd.DataFrame(lista_reproduccion)
df=pd.read_csv("empleados.csv",encoding="UTF-8")
#df=pd.read_json("productos_informatica.json")
print(df)
#print("columns",df.columns)
#print("values",df.values)
#print("head",df.head)
#print("tail",df.tail)
#print(df.iloc[0]) #primera columna
"""
for v in df.values:
    print(v[1])
"""    
#Salario medio
#print(f"Salario medio",{df["salario"].mean():.2f})
#print("Salario mas bajo",df["salario"].min())
#print("Salario mas alto",df["salario"].max())
print(df.sort_values(by=["edad"],ascending=False))


