from django import forms
from .models import QuestionQuiz, ChoiceQuiz


class Quizform(forms.ModelForm):

    model = QuestionQuiz, ChoiceQuiz

    fields = [
        "Add a question",
        "Insert choices related to questions"
    ]