import re
from django import http
import django
from django.shortcuts import render
from . import models
# Create your views here.
def home (request):
    try:
        hero=models.hero.objects.get(show=True)
        firstSection=models.firstSection.objects.get(show=True)
        statSection=models.statSection.objects.get(show=True)
        serviceSingle=models.serviceSingle.objects.all
        Service=models.Service.objects.get(show=True)
        Sermons_main_section=models.Sermons_main_section.objects.get(show=True)
        verset_main_page=models.verset_main_page.objects.get(show=True)
        evenement_main_page=models.evenement_main_page.objects.get(show=True)
        secteur_main=models.secteur_main.objects.get(show=True)
        secteur=models.secteur.objects.all

        context={'hero':hero, 'firstSection':firstSection, 'statSection':statSection,
        'serviceSingle':serviceSingle,
        'Service':Service,
        'Sermons_main_section':Sermons_main_section,
        'verset_main_page':verset_main_page,
        'evenement_main_page':evenement_main_page,
        'secteur_main':secteur_main,
        'secteur':secteur,
        'active':1}
    except:
        context={}
    return render(request,'home/index.html',context)

def contact(request):
    contact = models.contact_page.objects.get(show=True)
    context={'active':2, 'contact':contact,}
    return render(request,'home/contact.html',context)