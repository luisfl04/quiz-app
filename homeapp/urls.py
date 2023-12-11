from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = "index" ),
    path("<int:pk>/", views.DetailView.as_view(), name = "detail"),
    path("<int:pk>/", views.ResultsView.as_view(), name = "results"),
    path("<int:question_id>/vote/", views.vote, name = "vote"),
    path("create/", views.create, name = "create"),
    path("<int:question_id>/update/", views.update, name =  "update"),
    path("<int:question_id>/delete/", views.delete, name = "delete"),
]