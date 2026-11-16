import pandas as pd

df=pd.read_json("alumnos.json",encoding="UTF-8")
grupos=df.groupby("curso").agg(nota_mayor=("nota","max"),total_alumnos=("nombre","count"))
#print(df)
print(f"La nota media de los alumnos es de:  {df["nota"].mean():.2f}")
print(grupos)



