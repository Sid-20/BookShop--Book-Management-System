import sqlite3
MyBooks=sqlite3.connect('Book_Store.db')

curBooks=MyBooks.cursor()
#SQL Query to create the Table Books

sql1=''' CREATE TABLE Books(
  Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Title TEXT NOT NULL,
  Author TEXT(20) NOT NULL,
  Price REAL,
  Quantity REAL);'''
curBooks.execute(sql1)
print("The Table is created")
MyBooks.commit()
MyBooks.close()
