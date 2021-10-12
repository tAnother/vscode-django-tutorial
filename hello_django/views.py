from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import datetime
from hello_django.forms import LogMessageForm
from hello_django.models import LogMessage
from django.views.generic import ListView

# Create your views here.

# def home(request):
#     return render(request, "hello_django/home.html")

def about(request):
    return render(request, "hello_django/about.html")

def contact(request):
    return render(request, "hello_django/contact.html")


def greeting(request, name):
    return render(
        request,
        'hello_django/greeting.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello_django/log_message.html", {"form": form})


class HomeListView(ListView):
    '''Renders the home page with a list of all messages.'''
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
