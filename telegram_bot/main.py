import config
import random
import telebot

bot = telebot.TeleBot(config.token)

class Car:
    def __init__(self, brand, color): 
        self.brand = brand
        self.color = color

    def info(self):
        return f"This is a car with brand {self.brand} and color {self.color}"

@bot.message_handler(commands=['start'])
def hello(message):
    username = message.from_user.first_name
    bot.reply_to(message, f"Salam, {username}!")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, """
/start - Says hello
/info - Provides bot commands info
/said - Sends audio of Said
/master - Sends photo of Billie Herrington
/coin - Flips a coin
/car - <color> <brand> - Creates a car and sends info about it              
""")
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Nice photo")
    
        
@bot.message_handler(commands=['master'])    
def master(message):
 chat_id = message.chat.id
 with open("master.jpg", "rb") as photo:
        bot.send_photo(chat_id, photo, caption="Master of this gym")

@bot.message_handler(commands=['said'])
def said(message):
    chat_id = message.chat.id
    with open("said.mp3", "rb") as audio:
        bot.send_audio(chat_id, audio, caption="Саида позови")

@bot.message_handler(commands=['coin'])
def coin(message):
    coin = random.choice(['EAGLE', 'RESCHKA'])
    bot.reply_to(message, coin)

@bot.message_handler(commands=['car'])
def car(message):
    args = message.text.split()[1:]

    if len(args) != 2:
     bot.reply_to(message, "Please use the format: /car <color> <brand>")
     return
    
    color, brand = args
    new_car = Car(brand, color)

    bot.reply_to(message, new_car.info())

 

 
bot.infinity_polling()
