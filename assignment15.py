#Q.1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
#6. Authors
import sqlite3
conn = sqlite3.connect("database1.db")
cur = conn.cursor()
cmd1 = "Create table Book(bookId int(5) primary key,titleId int(5),locaton char(10));"
cmd2 = "Create table Titles(titleId int(5),publisherId int(5),foreign key(titleId) refrences Book(titleId));"
cmd3 = "Create table Publishers(publisherId int(5),zipcodeId int(4),foreign key(publisherId) refrences Titles(publisherId));"
cmd4 = "Create table Zipcodes(zipcideId int(5),zipcode int(4),foreign key(zipcode) refrences Publishers(zipcodeId));"
cmd5 = "Create table AuthorsTitles(authortitleId int(5),authorId int(4),titleId int(5),foreign key(titleId) refrences Titles(titleId));"
cmd6 = "Create table Authors(authorId int(5) primary key,fname char(10),foreign key(authorId) refrences AuthorsTitles(authorId));"
curs.execute(cmd1)
curs.execute(cmd2)
curs.execute(cmd3)
curs.execute(cmd4)
curs.execute(cmd5)
curs.execute(cmd6)

#Q.2- Insert values in the tables.
import sqlite3
conn = sqlite3.connect("database1.db")
cur = conn.cursor()
cmd1 = "insert into Book values(123,321,"Delhi");"
cur.execute(cmd1)
cmd1 = "insert into Book values(456,654,"Noida");"
cur.execute(cmd1)
cmd2 = "insert into Titles values(4561232,236);"
cur.execute(cmd2)
cmd2 = "insert into Titles values(4561235,736);"
cur.execute(cmd2)
cmd3 = "insert into Publishers values(4561232,8966);"
cur.execute(cmd3)
cmd3 = "insert into Publishers values(4561235,7966);"
cur.execute(cmd3)
cmd4 = "insert into Zipcodes values(8966,"pnb");"
cur.execute(cmd4)
cmd4 = "insert into Zipcodes values(7966,"jnb");"
cur.execute(cmd4)
cmd5 = "insert into AuthorsTitles values(1236,236);"
cur.execute(cmd5)
conn.commit()

#Q.3- Update any values in any of the tables. Print the original and updated values.
import sqlite3
conn = sqlite3.connect("database1.db")
cur = conn.cursor()
print("original values of table Book:")
cmd = "select * from Book;"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
print("updated values:")
cmd = "select * from Book;"
cur.execute(cmd)
for i in cur.fetchall():
        print(i)
print("original values of table Authors:")
cmd = "select * from Authors;"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)
cmd = update Authors set fname = "H.F.Korth" where authorld="Gyani"
cur.execute(cmd)
print("updated values of table Authors:")
cmd = "select * from Authors;"
cur.execute(cmd)
for i in cur.fetchall():
    print(i)