import sqlite3 as sql3
import pandas as pd
import csv

path=rf'./database.sqlite'
conn= sql3.connect(path)
cur = conn.cursor()
cur.execute("select * from English")

with open("database.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cur.description]) # write headers
    csv_writer.writerows(cur)
