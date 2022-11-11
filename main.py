import os
from flask import Flask, request, render_template
import telebot


Token = "5527319081:AAEa0iA0OFICPdxHwOWXmq4FctZ7VwL9Bss"
bot = telebot.TeleBot(Token)
server = Flask(__name__)


def vow(input_text):
    user_message = str(input_text).lower()
    translate = ""
    vow = ["a", "e", "i", "o", "u",]
    mfv = ['alf','alm','alv']
    mbbt = ['mb','bt']
    cs = ['cy','ce','ci']
    csh = ['cio','cea','cia']
    dge = ['dge']
    igh = ['igh']
    ph = ["ph"]
    tu = ["tu"]
    zh = ["zh"]
    tch = ["tch"]
    tion = ["tion"]
    x = ["x"]
    for letter in mfv:
        if letter == "alf":
            user_message = user_message.replace('alf','af')
        elif letter == "alm":
            user_message = user_message.replace('alm','am')
        elif letter == "alv":
            user_message = user_message.replace('alv','av')
        else:
            return user_message
    for letter in mbbt:
        if letter == 'bt':
            user_message = user_message.replace('bt','t')
        elif letter == "mb":
            user_message = user_message.replace('mb','m')
        else:
            return user_message
    for letter in cs:
        user_message = user_message.replace('cy','sy')
    for letter in cs:
        user_message = user_message.replace('ce','se')
    for letter in cs:
        user_message = user_message.replace('ci','si')
    for letter in csh:
        user_message = user_message.replace('cio','shio')
    for letter in csh:
        user_message = user_message.replace('cia','shia')
    for letter in csh:
        user_message = user_message.replace('cea','shea')
    for letter in dge:
        user_message = user_message.replace('dge','ge')
    for letter in igh:
        user_message = user_message.replace('igh','ay')
    for letter in ph:
        user_message = user_message.replace('ph','f')
    for letter in tu:
        user_message = user_message.replace('tu','ch')
    for letter in zh:
        user_message = user_message.replace('zh','j')
    for letter in tch:
        user_message = user_message.replace('tch','ch')
    for letter in tion:
        user_message = user_message.replace('tion','shen')
    for letter in x:
        user_message = user_message.replace('x','ks')
    for letter in user_message:
        if letter in vow:
            translate += letter + "z" + letter 
        else:
            translate += letter       
    return translate


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Please Enter your Phrase: ' )
    

@bot.message_handler(commands=['about'])
def about(message): 
    bot.reply_to(message,'''- WHAT is Zargari language?
+ Zargari language is an encoding based on language rules for secret communication between two or more people.

- WHERE and WHY?
+ In the past, some people in Iran used this type of language encryption so that others would not notice the conversation between them.

- WHAT'S going on?
+ Until today, this type of encoding has only been done on the basis of Persian language rules.
+ In this project, I try to create an advanced structure so that Latin languages can also be converted into the Zargari language.
+ You can join me to revive this language and spread it all over the world.

* The future is encrypted ;)''')


@bot.message_handler(func=lambda message:True, content_types=["text"])
def echo_message(message):
    bot.reply_to(message, vow(message.text))


@server.route("/" + Token, methods=["POST"])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return render_template("index.html"), 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://zargari-bot.herokuapp.com/' + Token)
    return render_template("index.html"), 200


if __name__ == "__main__":
    server.run(host:="0.0.0.0", port:=int(os.environ.get('PORT', 5000)))