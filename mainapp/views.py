from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')


def feedback(request):
    review_set = []

    for item in ClientReview.objects.all():
        item.number_of_stars = int(item.number_of_stars)
        item.number_of_stars = range(item.number_of_stars)
        review_set.append(item)
    context ={
        'review_set': review_set
    }
    return render(request, 'feedback.html', context)