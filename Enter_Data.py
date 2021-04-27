import sqlite3

MyBooks=sqlite3.connect('Book_Store.db')

curBooks=MyBooks.cursor()

n=int(input("Enter the number of books you want to store: "))
print("Enter the Data of the Books Stored: ")

for i in range(1,n+1):#BOOK Data Entered
  B_id=int(input("Enter the Book ID: "))
  t=input("Enter the Title of the Book: ")
  a=input("Enter the Author of the Book: ")
  prc=float(input("Enter the price of the Book: "))
  qt=int(input("Enter the Quantity of the Books: "))

  sql2='''INSERT INTO Books (Book_ID,Title,Author,Price,Quantity) VALUES(?,?,?,?,?);'''
  curBooks.execute(sql2,(B_id,t,a,prc,qt))
  

qtion=input('Do you Wish to add more books? (Y/N): ')
while qtion=='Y':
  B_id=int(input("Enter the Book ID: "))
  t=input("Enter the Title of the Book: ")
  a=input("Enter the Author of the Book: ")
  prc=float(input("Enter the price of the Book: "))
  qt=int(input("Enter the Quantity of the Books: "))

  sql3='''INSERT INTO Books (Book_ID,Title,Author,Price,Quantity) VALUES(?,?,?,?,?);'''
  curBooks.execute(sql3,(B_id,t,a,prc,qt))
  qtion=input('Do you Wish to add more books? (Y/N): ')
MyBooks.commit()
print("The Data has been entered")
MyBooks.close()


