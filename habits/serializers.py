from rest_framework.serializers import ModelSerializer
from habits.models import Habit
from habits.validators import (
    ChoiceRewardValidator,
    DurationValidator,
    PleasantHabitValidator,
    PeriodicityValidator,
    AbsenceValidator,
)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        ChoiceRewardValidator("related_habit", "reward")(data)
        DurationValidator("duration")(data)
        PleasantHabitValidator("related_habit", "pleasant_habit_sign")(data)
        PeriodicityValidator("periodicity")(data)
        AbsenceValidator("reward", "related_habit", "pleasant_habit_sigh")(data)
        return data
