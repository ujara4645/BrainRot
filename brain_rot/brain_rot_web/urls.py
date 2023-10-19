from django.urls import path

from . import views

app_name = "brain_rot_web"
urlpatterns = [
    path("", views.index, name="index"),
    path("results", views.results, name="results"),
    path("survey", views.survey, name="survey"),
    path("results/<int:game_id>", views.result_detail, name="results_details")
]