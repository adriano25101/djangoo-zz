from .models import Car
from django.shortcuts import render
def homeView(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'home.html', context)
# Create your views here.
