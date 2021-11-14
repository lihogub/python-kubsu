#!/usr/bin/env python3

import sqlite3
import cgi

conn = sqlite3.connect("cgi-bin/database.db")
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

# Fill tables
subject_list = [
    ('none',),
    ('физлицо',),
    ('юрлицо',),
    ('работник',),
    ('работодатель',),
]
cursor.executemany("INSERT INTO subject (name) VALUES (?);", subject_list)

codex_list = [
    ('none',),
    ('конституция',),
    ('уголовный',),
    ('трудовой',),
    ('налоговый',)
]
cursor.executemany("INSERT INTO codex (title) VALUES (?);", codex_list)

law_list = [
    (
        "Статья 64. Порядок и условия предоставления отсрочки или рассрочки по уплате налога, сбора, страховых взносов",
        "юрлицо", "налоговый"),
    ("Статья 4. Запрещение принудительного труда", "работник", "трудовой"),
    (
        "Статья 31. Граждане Российской Федерации имеют право собираться мирно, без оружия, проводить собрания, митинги и демонстрации, шествия и пикетирование.",
        "физлицо", "конституция"),
]

cursor.executemany('''
INSERT INTO law (text, subject_id, codex_id) VALUES 
    (
        ?,
        (SELECT id FROM subject WHERE name == ?),
        (SELECT id FROM codex WHERE title == ?)
    );    
''', law_list)

form = cgi.FieldStorage()
text = form.getfirst("text", "none")
subject = form.getfirst("subject", "none")
codex = form.getfirst("codex", "none")

cursor.execute('''
    INSERT INTO law (text, subject_id, codex_id) VALUES 
        (
            ?,
            (SELECT id FROM subject WHERE name == ?),
            (SELECT id FROM codex WHERE title == ?)
        );    
    ''', (text, subject, codex))

cursor.execute("select * from law;")
allRecords = cursor.fetchall()

cursor.execute("select text from subject s join law l on s.id == l.subject_id where s.name == 'физлицо';")
naturalRecords = cursor.fetchall()

cursor.execute("select title, count(*) from codex c left outer join law l on c.id == l.codex_id group by c.title")
groupedByCodexRecords = cursor.fetchall()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>""")

print("<h2>Все записи в базе законов</h2>")
[print(f'{record}<br>') for record in allRecords]
print("<br>")

print("<h2>Законы, где субъекты физлица</h2>")
[print(f'{record}<br>') for record in naturalRecords]
print("<br>")

print("<h2>Количество законов по кодексам</h2>")
[print(f'{record}<br>') for record in groupedByCodexRecords]

print("</body>")
print("</html>")

cursor.close()
conn.close()
