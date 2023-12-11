from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = "index" ),
    path("create/", views.create, name = "create"),
    path("<int:question_id>/", views.detail, name = "detail"),
    path("<int:question_id>/results/", views.results, name = "results"),
    path("<int:question_id>/vote/", views.vote, name = "vote"),
    path("<int:question_id>/update/", views.update, name =  "update"),
    path("<int:question_id>/delete/", views.delete, name = "delete"),
]