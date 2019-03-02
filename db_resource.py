import sqlite3
import os

DATABASE = "./database.db"


if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE breeder (id INTEGER PRIMARY KEY,fname TEXT);")
    cur.execute("CREATE TABLE dog (id INTEGER PRIMARY KEY,fname TEXT, breeder_id, age INTEGER, weight INTEGER , FOREIGN KEY(breeder_id) REFERENCES breeder(id));")
    conn.commit()
    cur.execute("INSERT INTO breeder(id,fname) VALUES('1','Tyson');")
    cur.execute("INSERT INTO breeder(id,fname) VALUES('2','Thomas');")
    cur.execute("INSERT INTO breeder(id,fname) VALUES('3','Jerry');")
    cur.execute("INSERT INTO dog(fname,breeder_id,age,weight) VALUES('Nicholas', '2', '40','2');")
    cur.execute("INSERT INTO dog(fname,breeder_id,age,weight)  VALUES('Elvin', '3', '20','1');")
    cur.execute("INSERT INTO dog(fname,breeder_id,age,weight)  VALUES('Jass', '4', '30','3');")
    conn.commit()
    conn.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

