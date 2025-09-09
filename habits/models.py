from django.db import models

from users.models import User


# Create your models here.
class Habits(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    place = models.TextField(verbose_name="Место")
    time_processing = models.PositiveIntegerField(
        verbose_name="Время, сек.", default=120
    )
    action = models.TextField(verbose_name="Действие")
    is_pleasant = models.BooleanField(verbose_name="Приятная привычка")
    fk_habits = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="ссылка на приятную привычку"
    )
    period = models.PositiveIntegerField(
        verbose_name="Частота выполнения привычки", default=1
    )
    reward = models.TextField(verbose_name="Вознаграждение")
    max_time_processing = models.PositiveIntegerField(
        verbose_name="Максимальное время на выполнение", default=50
    )
    is_public = models.BooleanField(verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.place
