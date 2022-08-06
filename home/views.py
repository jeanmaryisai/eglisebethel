import re
from django import http
import django
from django.shortcuts import render
from . import models
# Create your views here.
def home (request):
    hero=models.hero.objects.all
    return render(request,'home/index.html',{'hero':hero})