import sqlite3

conn = sqlite3.connect("cgi-bin/database.db")
cursor = conn.cursor()

cursor.execute("select * from law;")
allRecords = cursor.fetchall()

cursor.execute("select text from subject s join law l on s.id == l.subject_id where s.name == 'физлицо';")
naturalRecords = cursor.fetchall()

cursor.execute("select title, count(*) from codex c left outer join law l on c.id == l.codex_id group by c.title")
groupedByCodexRecords = cursor.fetchall()

cursor.close()
conn.close()

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
