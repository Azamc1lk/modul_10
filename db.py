import sqlite3

dp_connect = sqlite3.connect("sqlite3")

dp_cursor = dp_connect.cursor()

dp_cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
first_name REAL,
last_name TEXT)
""")

dp_cursor.execute("""
CREATE TABLE IF NOT EXISTS product(
id INTEGER PRIMARY KEY,
title TEXT,
price REAL)
""")

dp_cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY,
product_id, REAL ,
user_id, INTEGER)
""")

dp_cursor.execute("""
INSERT INTO users ("first_name", "last_name")
VALUES("Azamat", "Xolmirzayev")
""")

dp_cursor.execute("""
INSERT INTO users ("first_name", "last_name")
VALUES("Abdulvoris", "Zokirov")
""")

dp_cursor.execute("""
INSERT INTO users ("first_name", "last_name")
VALUES("Abduqodir", "Komilov" )
""")

dp_cursor.execute("""
    INSERT INTO product(title, price) VALUES ('apple', 500)

""")

dp_connect.commit()

dp_connect.close()