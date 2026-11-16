import pandas as pd

df=pd.read_csv("house.csv",encoding="UTF-8")
#print(df)
presupuesto=float(input("¿Cual es tu presupuesto: "))
filtro=df.query("price<=@presupuesto").sort_values(by=["price"],ascending=False)
print(filtro)


               