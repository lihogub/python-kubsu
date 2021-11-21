#!/usr/bin/env python3

from xml_functions import export_to_file
import sqlite3

conn = sqlite3.connect("cgi-bin/database.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("select * from law;")

rows = []
for row in cursor.fetchall():
    rows.append(dict(row))

export_to_file(rows, "cgi-bin/db_dump.xml")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
                <meta http-equiv="refresh" content="0; url=/cgi-bin/stats.py" />
            </head>""")
print("</html>")
