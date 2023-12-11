from django.db import models

class QuestionQuiz(models.Model):
    created_at = models.DateField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    question_txt = models.CharField(max_length = 200)
    description = models.TextField(max_length=200)   
    subject = models.CharField(max_length = 60)
    done = models.BooleanField(default = False)

    def __str__(self):
        return self.question_txt

class ChoiceQuiz(models.Model):
    question = models.ForeignKey(QuestionQuiz, on_delete = models.CASCADE)
    choice_txt = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_txt
