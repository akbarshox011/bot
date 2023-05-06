token="6151965984:AAFYYnaQxw8t-TmUqVxjttAh_zOpBdFBFYM"
import sqlite3

database = sqlite3.connect('database.sqlite')
cursor = database.cursor()


def setinfo(name,xotira, narx,rangi,turi):
    cursor.execute('''INSERT INTO users(name, xotira,narx,rangi,turi)
     VALUES (?, ?, ?,?,?)''', (name,xotira,narx,rangi,turi))
    database.commit()
    database.close()


name = input('ism kiriting: ')
xotira= input('xotira kiriting: ')
narx= int(input('narx kiriting: '))
rangi=input('rang kiriting:')
turi=('turini kiriting:')
setinfo