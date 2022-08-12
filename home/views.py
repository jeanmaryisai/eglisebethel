import re
from django import http
import django
from django.shortcuts import render
from . import models
from django.core.mail import send_mail
# Create your views here.
def home (request):
    try:
        live=models.live.objects.all().last
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
        'active':1,
        'live':live}
    except:
        context={}
    return render(request,'home/index.html',context)

def contact(request):
    errorpost=True
    contact = models.contact_page.objects.get(show=True)
    context={'contact':contact,'error':errorpost}
    if request.method=="POST":
        
        try:
            name= request.POST['name']
            msj= request.POST['message']
            email= request.POST['email']
            
            if msj != '':
                msj= f'{name} vous a laissez un message... </br> {msj}'
                send_mail('On vous laissez un message sur votre blog '
                    ,msj
                    ,'jeanmaryisai@gmail.com'
                    ,['jeanmaryisai@gmail.com',]
                    ,
                )
                errorpost=False
        except:
            pass
        context={'contact':contact,'error':errorpost,'name':name}
        return render(request,'home/contact.html',context)
        
            
    contact = models.contact_page.objects.get(show=True)
    context={'contact':contact,'error':errorpost}
    return render(request,'home/contact.html',context)

def about(request):
    secteur_main=models.secteur_main.objects.get(show=True)
    secteur=models.secteur.objects.all
    verset_main_page=models.verset_main_page.objects.get(show=True)
    about=models.about_page.objects.get(show=True)
    wrapper=models.wrapper_about_page.objects.all
    context={'about':about,'secteur_main':secteur_main,
    'secteur':secteur,
    'wrapper':wrapper,'verset':verset_main_page.v1}
    return render(request,'home/about.html',context)

def events(request):
    evenement_main_page=models.evenement_main_page.objects.get(show=True)
    evenement=models.evenement.objects.all().order_by('startdate').reverse
    context={'page':evenement_main_page,'event':evenement}
    return render(request,'home/eventsingle.html',context)

def sermons(request):
    sermon=models.Sermon.objects.all
    Sermons_main_section=models.Sermons_main_section.objects.get(show=True)
    context={'page':Sermons_main_section,'sermon':sermon}
    return render(request,'home/sermons.html',context)

def bay(request):
    bay=models.bay.objects.get(show=True)
    context={'bay':bay}
    return render(request,'home/bay.html',context)

def baylibre(request):
    bay=models.bay.objects.get(show=True)
    context={'bay':bay}
    return render(request,'home/baylibre.html',context)