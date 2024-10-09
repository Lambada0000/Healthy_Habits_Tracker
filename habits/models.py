from datetime import timedelta
from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        **NULLABLE,
    )
    place = models.CharField(max_length=100, verbose_name="Место выполнения привычки")
    time = models.TimeField(verbose_name="Начало выполнения привычки")
    action = models.TextField(verbose_name="Что нужно сделать")
    pleasant_habit_sign = models.BooleanField(
        verbose_name="Признак приятной привычки", default=False
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка", **NULLABLE
    )
    periodicity = models.SmallIntegerField(default=1, verbose_name="Периодичность")
    reward = models.CharField(
        max_length=150, verbose_name="Награда за выполнение", **NULLABLE
    )
    duration = models.DurationField(
        verbose_name="Продолжительность выполнения", default=timedelta(minutes=2)
    )
    is_published = models.BooleanField(verbose_name="Признак публикации", default=True)

    def __str__(self):
        return f"{self.user} будет {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
