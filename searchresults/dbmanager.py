import sqlite3
import globalvars as gv


def query(priority):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM recipes WHERE priorty=?", (priority,))

    rows = cur.fetchall()
    for row in rows:
        gv.resu.append(row)
