from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('resume', views.resume, name='resume'),
    path('contact', views.contact, name='contact')
]