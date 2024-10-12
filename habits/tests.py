from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.habit = Habit.objects.create(
            action="Побегать на прогулку", user=self.user, time="07:00:00", place="улица"
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            "action": "Принять участие в марафоне",
            "time": "12:00",
            "place": "зал кино",
            "periodicity": "2",
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "action": "Принять участие в марафоне",
            "time": "12:00",
            "place": "зал кино",
            "periodicity": "3",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("action"), "Принять участие в марафоне")

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{
                "id": self.habit.pk,
                "user": self.user.pk,
                "place": self.habit.place,
                "time": self.habit.time,
                "action": self.habit.action,
                "pleasant_habit_sign": False,
                "periodicity": self.habit.periodicity,
                "reward": None,
                "duration": "0" + str(self.habit.duration),
                "is_published": True,
                "related_habit": None,
            }]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
