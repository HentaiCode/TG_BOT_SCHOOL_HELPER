import telebot
from database.models import Jobs
from database.manage import db_session
import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('token')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я TGBOT-SchoolHelper,"
                                      f" я предназначен для помощи тебе в школьных делах(напоминания, поиск "
                                      f"работ, и так далее). Чтобы узнать подробны функции пиши /help")


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id, "Я бот-помощник, у меня есть функции:")
    bot.send_message(message.chat.id, '\n'.join(data))


@bot.message_handler(commands=['search_job_title', '/search_job_ScopeWork'])
def search_job_title(message):
    title = message.text.replace('/search_job_title', '')
    search_job(title=title)


def search_job(title=None, name_of_scope=None):
    if title:
        jobs = db_session.query(Jobs).all()
        print(jobs)


if __name__ == '__main__':

    with open('functions.txt', 'rt', encoding='utf-8') as f:
        data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

    bot.polling(none_stop=True)
