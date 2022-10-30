from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import NewVacancyForm
from .models import Resume


class NewResume(View):
    model = Resume
    form_class = NewVacancyForm
    template_name = 'newresume.html'

    def get(self, request, *arfs, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            form = self.form_class(initial={'author': request.user.id})
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponse(status=403)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            if request.user.is_authenticated and not request.user.is_staff:
                form = self.form_class({'description': request.POST.get('description'), 'author': request.user.id})
                if form.is_valid():
                    form.save()
                return redirect('/home')
            else:
                return HttpResponse(status=403)


class ResumesListView(View):
    template_name = 'resumes.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'resumes.html', context={'resumes': Resume.objects.all()})

