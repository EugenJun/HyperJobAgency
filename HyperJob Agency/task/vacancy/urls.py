from django.urls import path
from . import views

urlpatterns = [
    path('', views.VacanciesListView.as_view()),
    path('new', views.NewVacancyView.as_view()),
]
