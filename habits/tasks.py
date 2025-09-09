from celery import shared_task
from celery.worker.state import requests

from config.settings import TELEGRAM_BOT_TOKEN
from habits.models import Habits


@shared_task
def send_message(pk):
    habit = Habits.objects.get(pk=pk)
    text = (f'Пришло время сделать {habit.action} в {habit.place}, чтобы получить '
            f'{habit.reward if habit.reward else habit.fk_habits}')

    params = {'text': text,
              'chat_id': habit.user.chat_id_telegramm}

    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", params=params)