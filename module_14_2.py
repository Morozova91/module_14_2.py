# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователя.


import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER)''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", (i, f"User{i}", f"example{i}@gmail.com", i * 10, "1000"))


# for i in range(0, 9, 2):
#
#         cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i + 1))
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (i,))
#1 Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = 6")
#2 Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
count_users = cursor.fetchall()[0]
# print(count_users)
#3 Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchall()[0]
# print(sum_balance)
#4 Вывести в консоль средний баланс всех пользователя.
cursor.execute("SELECT AVG(balance) FROM Users")
avg = cursor.fetchall()[0]
print(avg)



connection.commit()
connection.close()
