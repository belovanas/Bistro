import config
import telebot

bot = telebot.TeleBot(config.token)
#fjtylui'
#Обработчик команд start и end
@bot.message_handler(content_types=["text"])
def say_hello(message):
    bot.send_message(message.chat.id, "Hello, guy")
#def say_bye(message):
    #if

if __name__ == '__main__':
    bot.polling(none_stop=True)