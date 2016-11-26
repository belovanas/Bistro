import config
import DataBase
import telebot

bot = telebot.TeleBot(config.token)

name = ""
address = ""

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
def invitation_to_registration(message):
    bot.send_message(message.chat.id, "Чтобы зарегистрироваться, введите ваши личные данные в следующем формате: \n"
                                      "Имя Телефон E-mail Адресс доставки")
    p = message.text
    pp = p.split(' ')
    name = p[0]
    phone = p[1]
    mail = p[2]
    adress = p[3]
    DataBase.add_user(name,phone,mail,adress)

if __name__ == '__main__':
    bot.polling(none_stop=True)