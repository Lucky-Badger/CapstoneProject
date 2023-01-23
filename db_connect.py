import psycopg2

conn = psycopg2.connect(
    host="http://localhost:5431",
    database="postgres",
    user="postgres",
    password="example_pswd")
    
cursor = conn.cursor()

cursor.execute('SELECT * FROM information_schema.tables')

rows = cursor.fetchall()
for table in rows:
    print(table)