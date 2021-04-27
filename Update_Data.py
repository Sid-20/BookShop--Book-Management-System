import sqlite3

MyBooks=sqlite3.connect('Book_Store.db')

curBooks=MyBooks.cursor()

def Update_Book(record,q,name):
  res=tuple(ele1-ele2 for ele1,ele2 in zip(record,q))
  print("The Data has been Updated")
  print("The Number of books with name {} left are: {} ".format(name,res))
  sql6='''UPDATE Books SET Quantity='"+res+"' WHERE Title='"+name+"' ; '''
  curBooks.execute(sql6)

MyBooks.commit()


