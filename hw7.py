import sqlite3 as sql3
with sql3.connect('employees.db') as connection:
    cursor = connection.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    ID STRING NOT NULL , 
    fulname INTEGER NOT NULL ,
    salary DATE 
    )''')
    cursor.execute('''INSERT INTO students(ID,fulname,salary)
     VALUES(0012,'Enessa',45000),(0022,'Gaukhar',50000),(0032,'Karina',48000),(0042,'Aliya',52000),(0052,'Erika',60000),
     (0062,'Bakulya',54000),(0072,'Kamilla',45000),(0082,'Adinay',50000),(0092,'Mariyam',48000),(00102,'Aliza',52000)''')

    cursor.execute('''SELECT rowid,* FROM students''')
    for row in cursor.fetchall():
        print(row)