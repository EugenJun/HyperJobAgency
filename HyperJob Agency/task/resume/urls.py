from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResumesListView.as_view()),
    path('new', views.NewResume.as_view())
]
