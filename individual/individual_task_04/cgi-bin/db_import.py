#!/usr/bin/env python3

from xml_functions import export_to_file, import_from_file
import sqlite3

item_list = import_from_file("cgi-bin/db_dump.xml")

conn = sqlite3.connect("cgi-bin/database.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS codex 
    (
        id INTEGER PRIMARY KEY,
        title varchar UNIQUE
    );''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subject 
        (
            id INTEGER PRIMARY KEY,
            name varchar UNIQUE
        );''')

cursor.execute('''CREATE TABLE IF NOT EXISTS law 
(
    id INTEGER PRIMARY KEY,
    text varchar UNIQUE,
    subject_id int,
    codex_id int,
    FOREIGN KEY(subject_id) REFERENCES subject(id),
    FOREIGN KEY(codex_id) REFERENCES codex(id)
);''')

cursor.executemany('''
    INSERT INTO law (text, subject_id, codex_id) VALUES 
        (
            :text,
            (SELECT id FROM subject WHERE name == :subject_id),
            (SELECT id FROM codex WHERE title == :codex_id)
        ) on conflict do nothing;    
    ''', item_list)

conn.commit()
cursor.close()
conn.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
                <meta http-equiv="refresh" content="0; url=/cgi-bin/stats.py" />
            </head>""")
print("</html>")
