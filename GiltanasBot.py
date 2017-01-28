import telebot
import tokenFile 

bot = telebot.TeleBot(tokenFile.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Привет', 'как ты?','ты играешь?')
    user_markup.row('как прошел твой день?', 'я люблю тебя', 'заспойлерить ведьмака')
    bot.send_message(message.from_user.id, 'Wellcome', reply_markup = user_markup)

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '...', reply_markup = hide_markup)

print(bot.get_me())
def log(message, answer):
    print("\n -----------------------")
    from datetime import datetime
    print(datetime.now())
    print("Message from [0] [1]. (id = [2]) \n Text = [3]".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    print(answer)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = 'Привет, любимая \xF0\x9F\x98\x98	';
    if message.text == 'Привет':
        answer = 'Привет, как твои дела лисенок';
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'ты играешь?':
        answer = "да, я играю в дотку(ради тебя я даже доту сворачиваю)"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'как ты?':
        answer = "я хорошо, кушаю бабушкины котлетки"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'как прошел твой день?':
        answer = "я сходил на пары/работу , вечером выпил пива с друзями в пабе/поиграл в дотку"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'я люблю тебя':
        answer = "я тоже люблю тебя, моя стесняшка"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == 'заспойлерить ведьмака':
        answer = 'Цири лесбиянка, Геральд и Йениффер умрут, но будут вместе, Дани жив и он император Нильф...'
        bot.send_message(message.chat.id, answer)
        log(message, answer)
        

bot.polling(none_stop = True, interval=0)
