from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Team,  Announcements, Attendance, Worklogs
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import 


def homePageView(request):
    return render(request, 'home1.html')


#class homePageView(TemplateView):
    # template_name = 'home1.html'

class trackingPageView(TemplateView):
    template_name = 'tracking.html'

class loadingPageView(TemplateView):
    template_name = 'loading.html'

class HomeDataView(ListView):
    model = Team
    template_name = 'hometeams.html'


class Attendance(ListView):
    queryset = Attendance.objects.all()
    template_name = 'attendanceee.html'

class Announcements(ListView):
    queryset = Announcements.objects.all()
    template_name = 'announcements.html'

class Worklogs_V(ListView):
    queryset = Worklogs.objects.all()
    template_name = 'worklogs.html'


class WorklogDV(DetailView):
    model = Worklogs
    template_name = 'worklog_dv.html'


"""@login_required(login_url = 'login')
def Worklogs_C(request):
    context ={}
    form = SampleForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request, "worklogs_add_post.html", context) """


class Worklogs_C(LoginRequiredMixin, CreateView):
    queryset = Worklogs.objects.all()
    template_name = 'worklogs_add_post.html'
    fields = ['task_id', 'details_of_execution', 'is_done', 'is_hold', 'member_id', 'remarks', 'git_url', 'gdocs_url', 'other_links', 'hours_taken', 'date']
    redirect_field_name = 'login'

# @login_required(login_url = 'user-login')
class Worklogs_U(UpdateView):
    model = Worklogs
    template_name = 'worklogs_edit.html'
    fields = ['details_of_execution', 'task_id']

# @login_required(login_url = 'user-login')
class Worklogs_D(DeleteView):
    model = Worklogs
    template_name = 'worklogs_delete.html'
    success_url = reverse_lazy('worklogswithhtml')




    



