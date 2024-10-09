from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habit_list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
