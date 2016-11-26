import sqlite3

conn = sqlite3.connect('Order.my.sqlite')

c = conn.cursor()


#Функция занесения пользователя в базу
def add_user(username,userphone,usermail,useradress):
    c.execute("INSERT INTO users (name,phone,mail,adress) VALUES ('%s','%s','%s','%s')" % (username,userphone,usermail,useradress))
    conn.commit()

name = "Andrew"
phone = "89012913813"
mail = "mail@mail.ru"
adress = "Rostov, Larina 7/2"

#Делаем запрос в базу
print("Список пользователей:\n")
add_user(name,phone,mail,adress)
c.execute('SELECT * FROM users')
row = c.fetchone()

c.close()
conn.close()
