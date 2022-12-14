"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu),
    path('resumes/', include('resume.urls')),
    path('vacancies/', include('vacancy.urls')),
    path('login', views.MyLoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('signup', views.MySignupView.as_view()),
    path('home', views.MyHomeView.as_view()),
    path('vacancy/', include('vacancy.urls')),
    path('resume/', include('resume.urls')),
]
