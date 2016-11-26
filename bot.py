import telebot
import sqlite3

token = '301583096:AAFIj_0jfY5Xoy8WivDoieZKSczIDCGO3zg'

bot = telebot.TeleBot(token)

name = ""
address = ""
email = ""
phone = ""


#Обработчик команд start и end
@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, "Привет)")


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
    conn = sqlite3.connect('Order.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name,phone,mail,adress) VALUES ('%s','%s','%s','%s')" % (username, userphone, usermail, useraddress))
    conn.commit()
    c.close()
    conn.close()


def registration_finished(message):
    add_to_base(name, phone, email, address)
    bot.send_message(message.chat.id, "Регистрация завершена!")

@bot.message_handler(regexp="Регистрация: ")
def catch_data(message):
    p = message.text
    pp = p.split(' ')
    global name, address, phone, email
    name = pp[1]
    phone = pp[2]
    email = pp[3]
    address = pp[4]
    registration_finished(message)


if __name__ == '__main__':
   bot.polling(none_stop=True)

