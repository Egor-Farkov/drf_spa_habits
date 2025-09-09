from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateApiView, HabitDestroyApiView,
                          HabitListApiView, HabitRetrieveApiView,
                          HabitUpdateApiView, PublicHabitListApiView)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListApiView.as_view(), name="list_habits"),
    path("new/", HabitCreateApiView.as_view(), name="new_habit"),
    path("public/", PublicHabitListApiView.as_view(), name="public_habits"),
    path("detail/<int:pk>", HabitRetrieveApiView.as_view(), name="detail_habit"),
    path("update/<int:pk>", HabitUpdateApiView.as_view(), name="update_habit"),
    path("delete/<int:pk>", HabitDestroyApiView.as_view(), name="delete_habit"),
]
