from rest_framework import serializers

from habits.models import Habits
from habits.validator import HabitsValidator


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = "__all__"
        validators = [HabitsValidator()]


class PublicHabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = (
            "action",
            "is_pleasant",
            "max_time_processing",
        )
