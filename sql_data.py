import pandas as pd
import sqlite3

csv_file_path = r"C:\Users\puruv\Desktop\genai_ds\bollywood_movie.csv"
df = pd.read_csv(csv_file_path)
conn = sqlite3.connect('bollywood_movies.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
    Title TEXT,
    Type TEXT,
    Release_Year INTEGER,
    Genre TEXT,
    Director TEXT,
    Production_House TEXT,
    Lead_Actors TEXT,
    Language TEXT,
    Budget_Millions REAL,
    Box_Office_Millions REAL,
    OTT_Platform TEXT,
    Runtime_Minutes INTEGER,
    No_of_Episodes INTEGER,
    IMDb_Rating REAL,
    Audience_Score INTEGER,
    Critics_Score INTEGER,
    Awards_Nominations INTEGER,
    Awards_Won INTEGER,
    Social_Media_Mentions INTEGER,
    User_Reviews_Count INTEGER,
    Viewership_Hours_Million REAL
)
''')

df.to_sql('movie', conn, if_exists='replace', index=False)
conn.commit()

query="select * from movie limit 5"
result=cursor.execute(query)

for row in result:
    print(row)

conn.close()