from django.views.generic import UpdateView
from django_celery_beat.models import PeriodicTask
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView, get_object_or_404)

from habits.models import Habits
from habits.paginators import HabitPagination
from habits.serializers import HabitsSerializer, PublicHabitsSerializer
from habits.services import replaces_create, make_replacements, create_schedule, create_task
from users.permissions import IsUser


# Create your views here.
class HabitCreateApiView(CreateAPIView):
    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)

        if not habit.is_pleasant:
            replacements = replaces_create()
            habit.frequency = make_replacements(habit.frequency, replacements)
            habit.save()

            if habit.user.chat_id_telegramm:
                schedule = create_schedule(habit.frequency)

                create_task(schedule, habit)



class PublicHabitListApiView(ListAPIView):
    serializer_class = PublicHabitsSerializer

    def get_queryset(self):
        return Habits.objects.filter(is_public=True)


class HabitListApiView(ListAPIView):
    serializer_class = HabitsSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)


class HabitRetrieveApiView(RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsUser,)


class HabitUpdateApiView(UpdateView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsUser,)

    def perform_update(self, serializer):
        habit = serializer.save(user=self.request.user)

        if not habit.is_pleasant:
            replacements = replaces_create()
            habit.frequency = make_replacements(habit.frequency, replacements)
            habit.save()

            if habit.user.chat_id_telegramm:
                task = get_object_or_404(PeriodicTask, name=f'я напоминаю о привычке {habit.pk} {habit.action}')
                schedule = create_schedule(habit.frequency)
                if task:
                    task.enabled = False
                    task.delete()

                create_task(schedule, habit)


class HabitDestroyApiView(DestroyAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsUser,)
