from django import forms
from .models import QuestionQuiz, ChoiceQuiz


class Quizform(forms.ModelForm):

    class Meta:
        model = QuestionQuiz

        fields = [
            "question_txt",
            "subject",
            "description",
        ]

    