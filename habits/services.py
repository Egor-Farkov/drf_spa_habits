import json

from django_celery_beat.models import CrontabSchedule, PeriodicTask


def replaces_create():
    m = '0'
    h = '9'
    x = h
    y = '0'
    z = str((int(x) + int(y)) // 2) if y != '0' else x
    d = '*'

    return {'m': m, 'h': h, 'x': x, 'y': y, 'z': z, 'd': d}


def make_replacements(text, replacements):
    for key, value in replacements.items():
        text = text.replace(key, value)

    return text


def create_schedule(cron: str):
    minute, hour, day_of_month, month_of_year, day_of_week = cron.split(' ')
    schedule, created = CrontabSchedule.objects.get_or_create(minute=minute, hour=hour, day_of_month=day_of_month,
                                                              month_of_year=month_of_year, day_of_week=day_of_week)

    return schedule


def create_task_habit(habit):

    if habit.period == 1:
        cron = '0 9 * * *'

    elif habit.period == 7:
        cron = '0 9 * * 1'

    elif habit.period == 30:
        cron = '0 9 1 * *'

    else:
        cron = '0 9 * * *'

    schedule = create_schedule(cron)


    PeriodicTask.objects.create(crontab=schedule,
                                name=f'я напоминаю о привычке {habit.pk} {habit.action}',
                                task='habits.tasks.send_message',
                                args=json.dumps([habit.pk]),
                                description='напоминание')

def update_schedule(habit):

    PeriodicTask.objects.filter(name__startswith = f'я напоминаю о привычке {habit.pk}').delete()
    create_task_habit(habit)


def delete_schedule(habit_pk):
    PeriodicTask.objects.filter(name__startswith=f'я напоминаю о привычке {habit_pk}').delete()


def get_habit_cron(number):
    if number == 1:
        return '0 9 * * *'

    elif number == 7:
        return '0 9 * * 1'

    elif number == 30:
        return '0 9 1 * *'

    else:
        return '0 9 * * *'


def create_task(schedule, habit):
    PeriodicTask.objects.create(crontab=schedule,
                                name=f'я напоминаю о привычке {habit.pk} {habit.action}',
                                task='habits.tasks.send_message',
                                args=json.dumps([habit.pk]),
                                description='напоминание')






