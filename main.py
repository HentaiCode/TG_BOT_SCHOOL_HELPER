import telebot
from telebot import types
from database.models import Jobs
from database.manage import db_session
import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('token')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup()
    button_help = types.KeyboardButton('/help')
    button_search_title = types.KeyboardButton('/search_job_title')
    button_search_scope = types.KeyboardButton('/search_job_ScopeWork')

    markup.row(button_search_title, button_search_scope)
    markup.row(button_help)

    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я TGBOT-SchoolHelper,"
                                      f" я предназначен для помощи тебе в школьных делах(напоминания, поиск "
                                      f"работ, и так далее). Чтобы узнать подробны функции пиши /help",
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id, "Я бот-помощник, у меня есть функции:")
    bot.send_message(message.chat.id, '\n'.join(data))


@bot.message_handler(commands=['search_job_title'])
def search_job_title1(message):
    bot.register_next_step_handler(message, search_job_title2)


def search_job_title2(message):
    jobs = search_job(title=message.text)
    for job in jobs:
        if job.is_private == 0:
            send = [job.title,
                    f'Направление: {job.scope_of_work}',
                    f'Тимлид: {job.team_leader_name}',
                    f'Участники: {job.accomplices}',
                    f'Закончено ли: {"да" if job.is_finished else "нет"}',
                    f'Выложили работу: {"".join(str(job.created_date).split(".")[:-1])}']
            bot.send_message(message.chat.id, '\n'.join(send))


@bot.message_handler(commands=['search_job_ScopeWork'])
def search_job_scopework1(message):
    bot.register_next_step_handler(message, search_job_scopework2)


def search_job_scopework2(message):
    jobs = search_job(name_of_scope=message.text)
    for job in jobs:
        if job.is_private == 0:
            send = [job.title,
                    f'Направление: {job.scope_of_work}',
                    f'Тимлид: {job.team_leader_name}',
                    f'Участники: {job.accomplices}',
                    f'Закончено ли: {"да" if job.is_finished else "нет"}',
                    f'Выложили работу: {"".join(str(job.created_date).split(".")[:-1])}']
            bot.send_message(message.chat.id, '\n'.join(send))


def search_job(title=None, name_of_scope=None):
    jobs = db_session.query(Jobs).all()
    ans = []

    if title:
        for job in jobs:
            if title in job.title:
                ans.append(job)
        return ans

    if name_of_scope:
        for job in jobs:
            if name_of_scope in job.scope_of_work:
                ans.append(job)
        return ans


if __name__ == '__main__':

    with open('functions.txt', 'rt', encoding='utf-8') as f:
        data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

    bot.polling(none_stop=True)
