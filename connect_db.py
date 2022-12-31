import pandas as pd
import sqlalchemy as db

engine = db.create_engine("mysql+mysqlconnector://root:Khongbiet?1@localhost:3306/")


# engine = db.create_engine("mysql+mysqlconnector://bee:Khongbiet?1@localhost/")
connection = engine.connect()
engine.execute('CREATE DATABASE vga_info;')

engine = db.create_engine("mysql+mysqlconnector://root:Khongbiet?1@localhost:3306/vga_info")
connection = engine.connect()

with open('info.csv', 'r') as file:
    df_info = pd.read_csv(file)
df_info.to_sql('info', con=engine)