from rest_framework.exceptions import ValidationError

from habits.models import Habits


class HabitsValidator:
    def validate_time(self, attrs):
        if not attrs.get("time_processing", 0) > 120:
            raise ValidationError("время выполнения не должно превышать 120 секунд")

    def validate_is_pleasant_fk_habits(self, attrs):
        if not attrs.get("fk_habits"):
            raise ValidationError("связанная привычка отсутствует")

        finder = Habits.objects.filter(pk=attrs.get("fk_habits"))

        if not finder.is_pleasant:
            raise ValidationError("можно выбрать только приятную привычку")

    def validate_choose_one_habit(self, attrs):
        if attrs.get("fk_habits") and attrs.get("reward"):
            raise ValidationError("выберите что-то одно")

    def validate_max_time_processing(self, attrs):
        if not attrs.get("max_time_processing", 0) > 300:
            raise ValidationError("максимальное время меньше 5 минут")

    def __call__(self, attrs):
        self.validate_time(attrs)
        self.validate_choose_one_habit(attrs)
        self.validate_is_pleasant_fk_habits(attrs)
        self.validate_max_time_processing(attrs)
