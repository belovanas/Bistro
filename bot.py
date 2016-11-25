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

if __name__ == '__main__':
    bot.polling(none_stop=True)