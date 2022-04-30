import telebot
from telebot import types
from database.models import Jobs, Schedule
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
    button_schedule = types.KeyboardButton('/schedule')

    markup.row(button_search_title, button_search_scope)
    markup.row(button_schedule)
    markup.row(button_help)

    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я TGBOT-SchoolHelper,"
                                      f" я предназначен для помощи тебе в школьных делах(напоминания, поиск "
                                      f"работ, и так далее). Чтобы узнать подробны функции пиши /help",
                     reply_markup=markup)


@bot.message_handler(commands=['schedule'])
def schedule_starter(message):
    bot.register_next_step_handler(message, schedule_starter_worker)


def schedule_starter_worker(message):
    message_str = message.text.lower().split(',')
    schedule = return_lessons(message_str[0], message_str[1], message_str[2])
    if schedule != 'Извини, но ты неправильно ввел данные или такого дня/класса просто ещё нет':
        schedule = list(map(lambda lesson: f'Пара {str(schedule.split(", ").index(lesson) + 1)}: {lesson}',
                            schedule.split(', ')))
        bot.send_message(message.chat.id, '\n'.join(schedule))
    else:
        bot.send_message(message.chat.id, schedule)


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id, "Я бот-помощник, у меня есть функции:")
    bot.send_message(message.chat.id, '\n'.join(data))


@bot.message_handler(commands=['search_job_title'])
def search_job_title_starter(message):
    bot.register_next_step_handler(message, search_job_title_worker)


def search_job_title_worker(message):
    jobs = search_job(title=message.text)
    if jobs == 'Извини, но того, что ты искал нет в базе данных, попробуй ее раз или поищи по-другому))':
        bot.send_message(message.chat.id,
                         'Извини, но того, что ты искал нет в базе данных, попробуй ее раз или поищи по-другому))')
        return
    for job in jobs:
        if job.is_private == 0:
            send = [job.title,
                    f'Направление: {job.scope_of_work}',
                    f'Тимлид: {job.team_leader_name}',
                    f'Участники: {job.accomplices}',
                    f'Закончено ли: {"да" if job.is_finished else "нет"}',
                    f'Выложили работу: {"".join(str(job.created_date).split(".")[:-1])}',
                    f'Сама работа:\n{message.chat.id}']
            bot.send_message(message.chat.id, '\n'.join(send))


@bot.message_handler(commands=['search_job_ScopeWork'])
def search_job_scopework_starter(message):
    bot.register_next_step_handler(message, search_job_scopework_worker)


def search_job_scopework_worker(message):
    jobs = search_job(name_of_scope=message.text)
    if jobs == 'Извини, но того, что ты искал нет в базе данных, попробуй ее раз или поищи по-другому))':
        bot.send_message(message.chat.id,
                         'Извини, но того, что ты искал нет в базе данных, попробуй ее раз или поищи по-другому))')
        return
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
    return 'Извини, но того, что ты искал нет в базе данных, попробуй ее раз или поищи по-другому))'


def return_lessons(week_number, grade, day_of_the_week):
    schedules = db_session.query(Schedule).all()
    day_of_the_week = day_of_the_week.lower().strip()
    for schedule in schedules:
        if schedule.grade == grade.strip().upper() and schedule.week_number == int(week_number.strip()):
            if day_of_the_week == 'понедельник':
                return schedule.monday
            elif day_of_the_week == 'вторник':
                return schedule.tuesday
            elif day_of_the_week == 'среда':
                return schedule.wednesday
            elif day_of_the_week == 'четверг':
                return schedule.thursday
            elif day_of_the_week == 'пятница':
                return schedule.friday
            elif day_of_the_week == 'суббота':
                return schedule.saturday
            elif day_of_the_week == 'воскресенье':
                return schedule.sunday
    return 'Извини, но ты неправильно ввел данные или такого дня/класса просто ещё нет'


if __name__ == '__main__':

    with open('functions.txt', 'rt', encoding='utf-8') as f:
        data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

    bot.polling(none_stop=True)
