from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import QuestionQuiz, ChoiceQuiz
from .form import Quizform
from django.views import generic


def index(request):
    latest_question_list = QuestionQuiz.objects.all()
    template = "index.html"
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, template, context)
    
def detail(request, question_id):
    question = get_object_or_404(QuestionQuiz, pk = question_id)
    template = "detail.html"
    context = {
        "question": question
    }
    return render(request, template, context)           

def results(request, question_id):
    question = get_object_or_404(QuestionQuiz, pk = question_id)
    template = "results.html"
    context = {
        "question": question,
    }
    return render(request, template, context)

def vote(request, question_id):
    question = get_object_or_404(QuestionQuiz, pk = question_id)
    try:
        selected_choice = question.choicequiz_set.get( pk = request.POST["choicequiz"])
    except(KeyError, ChoiceQuiz.DoesNotExist):
        return render(
            request,
            "detail.html",
            {
                "question":question,
                "error_message": "You don`t select a choice."
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args = (question.id,)))
    
def create(request):
    form =  Quizform(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("index"))
    
    template = "new.html"
    context = {
        "form": form,
        "action": "Create"
    }
    return render(request, template, context)

def update(request, question_id):
    question = get_object_or_404(QuestionQuiz, pk = question_id)
    form = Quizform(request.POST or None, instance = question)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("index"))
    
    template = "new.html"
    context = {
        "form": form,
        "action": "To edite"
    }
    return render(request, template, context)

def delete(request, question_id):
    question = get_object_or_404(QuestionQuiz, pk = question_id)
    question.delete()
    return HttpResponseRedirect(reverse("index"))
