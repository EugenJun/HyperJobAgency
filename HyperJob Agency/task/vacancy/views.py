from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import NewVacancyForm
from .models import Vacancy


class NewVacancyView(View):
    form_class = NewVacancyForm
    template_name = 'newvacancy.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            form = self.form_class(initial={'author': request.user.id})
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponse(status=403)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            if request.user.is_authenticated and request.user.is_staff:
                form = self.form_class({'description': request.POST.get('description'), 'author': request.user.id})
                if form.is_valid():
                    form.save()
                return redirect('/home')
            else:
                return HttpResponse(status=403)


class VacanciesListView(View):
    template_name = 'vacancies.html'

    def get(self, request, *args, ** kwargs):
        return render(request, 'vacancies.html', context={'vacancies': Vacancy.objects.all()})

