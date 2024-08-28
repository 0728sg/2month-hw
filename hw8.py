import sqlite3

conn = sqlite3.connect('person.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments (DepartmentID)
)
''')

cursor.executemany('''
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (?, ?)
''', [
    (101, 'HR'),
    (102, 'IT'),
    (103, 'Sales')
])

cursor.executemany('''
INSERT INTO Employees (FirstName, LastName, DepartmentID) VALUES (?, ?, ?)
''', [
    ('John', 'Doe', 101),
    ('Jane', 'Smith', 101),
    ('Alice', 'Johnson', 102),
    ('Bob', 'Brown', 102),
    ('Charlie', 'Davis', 103),
    ('Eva', 'Wilson', 103)
])

conn.commit()

cursor.execute('''
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
''')
all_employees = cursor.fetchall()

cursor.execute('''
SELECT Employees.FirstName, Employees.LastName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'IT'
''')
it_employees = cursor.fetchall()
conn.close()

all_employees, it_employees
