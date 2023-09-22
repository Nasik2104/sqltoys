import sqlite3

with sqlite3.connect('toys.db') as db:
    cr = db.cursor()
    cr.execute('''CREATE TABLE IF NOT EXISTS toys (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT,
                    price REAL,
                    stock_quantity INTEGER
                )''')

    cr.execute(
        """INSERT INTO toys (name, type, price, stock_quantity) VALUES
        ('Пес Патрон', 'домашні улюбленці', 9.99, 5),
        ('Мяка ведмедиця', 'ведмедик', 10.99, 0), 
        ('Маленький ведмедик', 'ведмедик', 9.99, 50),
        ('Великий ведмедик', 'ведмедик', 20.99, 50),
        ('зайчик Star', 'Домашні улюбленці', 19.99, 30),
        ('SpongeBob', 'МультФільми', 29.99, 9),
        ('Patrik', 'МультФільми', 12.99, 3)
        """
    )
    
    cr.execute("""
               DELETE FROM toys WHERE stock_quantity <= 0
               """)
    
    cr.execute("""
               UPDATE toys SET stock_quantity = stock_quantity + 5 WHERE name == 'Patrik'
               """)
    
    cr.execute("""
               SELECT name FROM toys 
               """)
    result = cr.fetchall()
    for res in result:
        print(res[0])
        
    cr.execute("""
               SELECT name, price FROM toys WHERE price <= 20 
               """)
    result = cr.fetchall()
    for res in result:
        print(f"{res[0]} - {res[1]}")
        
    cr.execute("""
               SELECT type, SUM(stock_quantity) FROM toys GROUP BY type
               """)
    result = cr.fetchall()
    for res in result:
        print(f"Тип:{res[0]} - К-сть:{res[1]}")
        
    cr.execute("""
               SELECT name, stock_quantity FROM toys WHERE stock_quantity < 10
               """)
    result = cr.fetchall()
    for res in result:
        print(f"Назва:{res[0]} - К-сть:{res[1]}")
