from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView


from django.http import HttpResponse

# from .models import announcements
def Sampleview(request):
    return HttpResponse('Welcome to demo page')


class display(ListView):
    #queryset = announcements.objects.all()
    template_name = 'display.html'


class Ann_cv(CreateView):
    # model = announcements
    template_name = 'add_post.html'
    fields = '__all__'


#def display(request):
    #st=announcements.objects.all() # Collect all records from table
    #return render(request,'display.html',{'st':st})
