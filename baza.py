import psycopg2
import json

conn = psycopg2.connect(host="localhost", user="postgres", dbname="test")
print("Opened successfully")
cur = conn.cursor()
cur.execute("select * from  tabela1 where id = 1");
rows = cur.fetchall()
print(type(json.dumps(rows)))
for row in rows:
    print("id = ", row[0])
    print("ime = ", row[1])
    print("prezime", row[2])
    print("email", row[3], "\n")

conn.close()
