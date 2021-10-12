from collections import namedtuple
from django.urls import path
from django.urls.resolvers import URLPattern
from hello_django import views
from hello_django.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5], 
    context_object_name="message_list",
    template_name="hello_django/home.html"
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.greeting, name="greeting"),
    path("about/", views.about, name="aboutus"),
    path("contact/", views.about, name="contact"),
    path("log/", views.log_message, name="log"),
]
