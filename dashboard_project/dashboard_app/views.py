from django.shortcuts import render
from .models import *

def index(request):
    users = UserC.objects.all().count()
    context = {"users": users}
    return render(request, 'grid1.html', context=context)

def grid2(request):
    users = UserC.objects.all().count()
    context = {"users": users}
    return render(request, 'grid2.html', context=context)

def grid3(request):
    users = UserC.objects.all().count()
    context = {"users": users}
    return render(request, 'grid3.html', context=context)
