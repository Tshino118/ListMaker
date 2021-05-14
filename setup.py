import sqlite3 as sql3

path=rf'./database.sqlite'
conn= sql3.connect(path)
cur = conn.cursor()

cur.execute(
    '''CREATE TABLE English(
        sentence TEXT PRIMARY KEY,
        description TEXT
    )'''
)
conn.commit()
conn.close()