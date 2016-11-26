import telebot
import sqlite3
import datetime

#Токен созданного бота
token = '301583096:AAFIj_0jfY5Xoy8WivDoieZKSczIDCGO3zg'

bot = telebot.TeleBot(token)

o_status = ""

#Обработчик команды start
@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, "Привет)")

@bot.message_handler(commands=['help'])
def print_commands(message):
    f = open("commandlist.txt")
    line = f.readline()
    res = line
    while line:
        line = f.readline()
        res = res + line
    bot.send_message(message.chat.id, res)
    f.close()


#Обработчик команды finish
@bot.message_handler(commands=['finish'])
def say_bye(message):
    bot.send_message(message.chat.id, "Пока!")
    bot.leave_chat(message.chat.id)


#Обработчик команды SignUp
@bot.message_handler(commands=['signup'])
def invitation_to_name(message):
    bot.send_message(message.chat.id, "Чтобы зарегистрироваться, введите следующие данные:\n"
                                      "Имя: Ваше имя\n"
                                      "Телефон: Мобильный телефон в формате 8-XXX-XX-XX\n"
                                      "E-mail: E-mail в формате email@gmail.com\n"
                                      "Адрес: Адрес для доставки\n"
                                      "Данные должны быть введены в формате:\n"
                                      "Регистрация: Имя Телефон E-mail Адрес")


def add_to_base(username, userphone, usermail, useraddress):
    conn = sqlite3.connect('BistroBotBase.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO users (name,phone,email,address) VALUES ('%s','%s','%s','%s')" % (username, userphone, usermail, useraddress))
    conn.commit()
    c.close()
    conn.close()


@bot.message_handler(regexp="Регистрация: ")
def catch_data(message):
    p = message.text
    pp = p.split(' ')
    name = pp[1]
    phone = pp[2]
    email = pp[3]
    address = pp[4]
    add_to_base(name, phone, email, address)
    bot.send_message(message.chat.id, "Регистрация завершена! Ваш заказ поступил в обработку!\n" +
                     "Время заказа: " + str(datetime.datetime.now()) + "\n" +
                     "Имя клиента: " + name + "\n" +
                     "Адрес доставки: " + address + "\n" +
                     "Телефон: " + phone + "\n"
                                           "Блюда: "  + "\n"
                                                               "Результат обработки заказов будет отправлен Вам на почту.")
    global o_status
    o_status = "Обработка"

@bot.message_handler(commands=['status'])
def order_status(message):
    if (o_status == "Обработка"):
        bot.send_message(message.chat.id, "Заказ обрабатывается.")
    if (o_status == "Выполнение"):
        bot.send_message(message.chat.id, "Заказ выполняется.")
    if (o_status == "Доставка"):
        bot.send_message(message.chat.id, "Заказ доставляется.")
    if (o_status == ""):
        bot.send_message(message.chat.id, "Нет текущего заказа.")

if __name__ == '__main__':
   bot.polling(none_stop=True)

