#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import random
import pyowm


greetings = ["Привет", "Здравствуй"]
how_are_you = ["Отлично"]

token ="860607191:AAHpGqH7EWkLM2aND8ArFwFfU_VdPB0rubA"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хочешь узнать погоду? воспользуйся строкой /weather')

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "Отлично, в каком городе желаете посмотреть погоду?")
    bot.register_next_step_handler(city, weath)



def weath(message):
    owm = pyowm.OWM("4f7727b6aa13a19b758007c7b12651d5")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Ух!Погода тут прекрасна! Сейчас " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Доброго времени суток :), " + message.chat.first_name)

@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id, random.choice(greetings) + ", " + message.chat.first_name)
    elif message.text == "Как дела?":
        bot.send_message(message.chat.id, random.choice(how_are_you))



@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "Отлично, в каком городе желаете посмотреть погоду?")
    bot.register_next_step_handler(city, weath)



def weath(message):
    owm = pyowm.OWM("4f7727b6aa13a19b758007c7b12651d5", language="ru")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Ух!Погода тут прекрасна! Сейчас в городе " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")


if __name__ == "__main__":
    bot.polling(none_stop=True)
