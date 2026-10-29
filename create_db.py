import sqlite3

conn = sqlite3.connect('company_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL,
    hire_date TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    product TEXT NOT NULL,
    amount INTEGER NOT NULL,
    sale_date TEXT NOT NULL,
    FOREIGN KEY(employee_id) REFERENCES employees(id)
)
''')

employees_data = [
    (1, 'Alice Smith', 'Engineering', 95000, '2021-03-15'),
    (2, 'Bob Johnson', 'Sales', 75000, '2020-07-01'),
    (3, 'Charlie Brown', 'Engineering', 105000, '2019-11-20'),
    (4, 'Diana Prince', 'HR', 65000, '2022-01-10'),
    (5, 'Evan Wright', 'Sales', 80000, '2023-05-22')
]
cursor.executemany('INSERT OR IGNORE INTO employees VALUES (?,?,?,?,?)', employees_data)

sales_data = [
    (1, 2, 'Software License', 5000, '2024-01-15'),
    (2, 2, 'Consulting', 12000, '2024-02-10'),
    (3, 5, 'Software License', 8000, '2024-01-20'),
    (4, 5, 'Hardware', 3000, '2024-03-05'),
    (5, 2, 'Consulting', 15000, '2024-03-12')
]
cursor.executemany('INSERT OR IGNORE INTO sales VALUES (?,?,?,?,?)', sales_data)

conn.commit()
conn.close()
print("Database created successfully with mock data!")