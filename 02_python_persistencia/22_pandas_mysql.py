import pandas as pd
import mysql.connector as con 
db=con.connect(
  host="localhost", 
  user="root", 
  password="root", 
  port=3306, 
  database="mundo")
df=pd.read_sql("Select * from paises",db)
print(df)
db.close()