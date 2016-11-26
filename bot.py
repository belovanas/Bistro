import config
import telebot

bot = telebot.TeleBot(config.token)
#fjtylui'
#Обработчик команд start и end
@bot.message_handler(commands=['start'])
def say_hello(message, update):
    bot.send_message(update.message.chat.id, "Привет)")

@bot.message_handler(commands=['finish'])
def say_bye(message):
    bot.send_message(message.chat.id, "Пока!")
    bot.leave_chat(message.chat.id)

#Обработчик команды SignUp
@bot.message_handler(commands=['signup'])
def invitation_to_registration(message):
    bot.send_message(message.chat.id, "Пожалуйста, введите свое имя: ")

@bot.message_handler(content_types=["text"])
def catch_name(message):
    name = message.text
    bot.send_message(message.chat.id, text=name)

if __name__ == '__main__':
    bot.polling(none_stop=True)