import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="example_pswd")
    
cursor = conn.cursor()

cursor.execute('SELECT * FROM information_schema.tables')

rows = cursor.fetchall()
for table in rows:
    print(table)

#docker run --name postgres -e POSTGRES_PASSWORD=example_pswd -p 5432:5432 -d postgres