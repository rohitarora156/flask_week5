import sqlite3

connection = sqlite3.connect('data.db') #name of the connected file

cursor = connection.cursor() # assesing , executing query ,and storing the result 

create_table = "CREATE TABLE users (id int,username test,password text)"
cursor.execute(create_table)

user = (1,'Sara','abcd')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)


users = [
    (2,'Sra','abce'),
    (3,'Jia','xyz')
]
cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()