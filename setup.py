import sqlite3 as sql3
import os.path
path=rf'./database.sqlite'
isfile=os.path.isfile(path)
if isfile:
    pass
else:
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
