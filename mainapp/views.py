from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')


def feedback(request):
    review_set = []

    for item in ClientReview.objects.all().order_by('?'):
        item.number_of_stars = int(item.number_of_stars)
        item.number_of_stars = range(item.number_of_stars)
        review_set.append(item)
    context ={
        'review_set': review_set
    }
    return render(request, 'feedback.html', context)


def resume(request):
    context = {
        'resume': Resume.objects.all().last()
    }
    return render(request, 'resume.html', context)


def contact(request):
    context = {
        
    }

    if request.method == 'POST':
        c = Contact()
        c.full_name = request.POST.get('full_name')
        c.email = request.POST.get('email')
        c.phone_number = request.POST.get('phone_number')
        c.message = request.POST.get('message')
        c.save()
    return render(request, 'contact.html', context)