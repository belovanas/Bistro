import config
import telebot

bot = telebot.TeleBot(config.token)

name = ""
address = ""
email = ""
phone = ""

#fjtylui'
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
    bot.send_message(message.chat.id, "Пожалуйста, введите свое имя в формате Имя: Иван")

@bot.message_handler(regexp="Имя:")
def catch_name(message):
    p = message.text
    pp = p.split(' ')
    name = pp[1]
    bot.send_message(message.chat.id, "Имя " + name)
    bot.send_message(message.chat.id, name + ", введите свой адрес в формате Адрес: Зорге,1,д.2")

@bot.message_handler(regexp="Адрес:")
def catch_address(message):
    p = message.text
    pp = p.split(' ')
    address = pp[1]
    bot.send_message(message.chat.id, "Адрес " + address)
    bot.send_message(message.chat.id, name + ", введите свой телефон в формате Телефон: 123456789")

@bot.message_handler(regexp="Телефон:")
def catch_phone(message):
    p = message.text
    pp = p.split(' ')
    phone = pp[1]
    bot.send_message(message.chat.id, "Телефон " + phone)


if __name__ == '__main__':
    bot.polling(none_stop=True)