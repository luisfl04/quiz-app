from django.db import models

class QuestionQuiz(models.Model):
    created_at = models.DateField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    question_txt = models.CharField(max_length = 200)
    pub_date = models.DateField("date of publication")
    subject = models.CharField(max_length = 60)

    def __str__(self):
        return self.question_txt

class ChoiceQuiz(models.Model):
    question = models.ForeignKey(QuestionQuiz, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True )
    update_at = models.DateTimeField(auto_now = True )
    choice_txt = models.CharField(max_length = 200)
    vote = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_txt
