#Connect to SQLite3
import sqlite3
import Enter_Data
import Update_Data



MyBooks=sqlite3.connect('Book_Store.db')

curBooks=MyBooks.cursor()



def buy_Book():
  name=input("Enter the book you want to buy: ")
  sql4=''' SELECT Quantity FROM Books WHERE Title= ?; '''
  curBooks.execute(sql4,(name,))
  record=curBooks.fetchone() #Number of books available
  print("The Number of books available are: {} ".format(record))
  q_tity= int(input("How many books do you want: "))
  q=(q_tity,) #Number of books bought
  sql5=''' SELECT Price FROM Books WHERE Title=?; '''
  curBooks.execute(sql5,(name,))
  book=curBooks.fetchone()
  print("The Price of one book is: ",book)
  res = tuple(ele1 * ele2 for ele1, ele2 in zip(q,book))
  print("Your Total Bill is : " + str(res))
  Update_Data.Update_Book(record,q,name)
  MyBooks.commit()
  
    
y='yes'
print("Hello Sir, Welcome to BookShop!! These are the list of books that are available")
sql7='''SELECT * FROM Books;'''
curBooks.execute(sql7)
List_Books=curBooks.fetchall()
for B in List_Books:
  print(B)
print("How Can I help you?: ")
buy_Book()
while y=='yes':
  y=input("Do You need anything else? (yes,no): ")
  if y=='yes':
    buy_Book()
  else:
    print("Thank You for shopping with us")
    break
MyBooks.commit()
MyBooks.close()



