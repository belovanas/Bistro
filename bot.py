import config
import telebot

bot = telebot.TeleBot(config.token)
#fjtylui'
#Обработчик команд start и end
@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, "Hello, guy!")

@bot.message_handler(commands=['finish'])
def say_bye(message):
    bot.send_message(message.chat.id, "Bye, friend!")
    bot.leave_chat(message.chat.id)

#Обработчик команды SignUp
@bot.message_handler(commands=['signup'])
def invitation_to_registration(message):
    bot.send_message(message.chat.id, "Please, enter your name: ")

@bot.message_handler(content_types=["text"])
def catch_name(message):
    name = message.text

if __name__ == '__main__':
    bot.polling(none_stop=True)