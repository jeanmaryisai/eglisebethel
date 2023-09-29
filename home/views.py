import json
from django.shortcuts import redirect
from django.shortcuts import render
from . import models
from django.core.mail import send_mail
from decimal import Decimal
from django.db.models import Count, Q
from . import utils
# Create your views here.
def home (request):
    try:
        live=models.live.objects.all().filter(show=True)
    except:
        live={}
    hero=models.hero.objects.get(show=True)
    firstSection=models.firstSection.objects.get(show=True)
    statSection=models.statSection.objects.get(show=True)
    serviceSingle=models.serviceSingle.objects.all().filter(show=True)
    Service=models.Service.objects.get(show=True)
    Sermons_main_section=models.Sermons_main_section.objects.get(show=True)
    verset_main_page=models.verset_main_page.objects.get(show=True)
    evenement_main_page=models.evenement_main_page.objects.get(show=True)
    secteur_main=models.secteur_main.objects.get(show=True)
    secteur=models.secteur.objects.all().filter(show=True)
    
    e1=utils.ev(1)
    e2=utils.ev(2)
    e3=utils.ev(3)

    context={'hero':hero, 'firstSection':firstSection, 'statSection':statSection,
    'serviceSingle':serviceSingle,
    'Service':Service,
        'Sermons_main_section':Sermons_main_section,
        'verset_main_page':verset_main_page,
        'evenement_main_page':evenement_main_page,
        'secteur_main':secteur_main,
        'secteur':secteur,
        'active':1,
        'live':live,
        'e1':e1,
        'e2':e2,
        'e3':e3,}
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
                msj= f'{name} vous a laissez un message... <br> {msj}'
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
    'wrapper':wrapper}

    try:
        context['bio']=models.article.objects.filter(show=True).get(isprimary=True).paragraphs[0].text[:150]
        context['slugArticle']=models.article.objects.filter(show=True).get(isprimary=True).slug
    except:
        context['verset']=verset_main_page.v1
    return render(request,'home/about.html',context)

def events(request):
    evenement_main_page=models.evenement_main_page.objects.get(show=True)
    evenement=models.evenement.objects.all().order_by('startdate').reverse
    context={'page':evenement_main_page,'event':evenement}
    return render(request,'home/events.html',context)

def singlevents(request,slug):
    evenement_main_page=models.evenement_main_page.objects.get(show=True)
    evenement=models.evenement.objects.get(slug=slug)
    imgs=evenement.album.all
    context={'page':evenement_main_page,'event':evenement,'imgs':imgs,}
    return render(request,'home/eventsingle.html',context)

def sermons(request,slug):
    
    tags=models.tag.objects.all()
    Sermons_main_section=models.Sermons_main_section.objects.get(show=True)
    context={'page':Sermons_main_section,'tags':tags}
    try:
        sermonJ=models.Sermon.objects.get(slug=slug)
        list=utils.matches(sermonJ)['list']
        sermon=models.Sermon.objects.all().exclude(title=sermonJ)
        context['sermonJ']=sermonJ
        context['list']=list
    except:
        try:
            slug=slug[:-2]
            slugTest=models.tag.objects.get(title=slug)
            xx=utils.matchOne(slug)
            context['sermon']=xx
            context['tag']=slug
        except:
            query = request.GET.get('q', '')  # Récupérez le terme de recherche de la requête GET
            # Effectuez une recherche dans les champs désirés
            sermons = models.Sermon.objects.filter(
                Q(title__icontains=query) |  # Recherche dans le titre (insensible à la casse)
                # Q(sous_titre__icontains=query) |  # Recherche dans le sous-titre (insensible à la casse)
                Q(orator__icontains=query) |  # Recherche dans l'auteur (insensible à la casse)
                Q(youtubeurl__icontains=query) |  # Recherche dans le contenu (insensible à la casse)
                Q(tags__title__icontains=query)  # Recherche dans les tags (insensible à la casse)
            )

            # Annoter les résultats avec le nombre d'occurrences du terme de recherche
            sermons = sermons.annotate(num_occurrences=Count(
                'title', filter=Q(title__icontains=query)) +
                # Count('sous_titre', filter=Q(sous_titre__icontains=query)) +
                Count('orator', filter=Q(orator__icontains=query)) +
                Count('youtubeurl', filter=Q(youtubeurl__icontains=query)) +
                Count('tags', filter=Q(tags__title__icontains=query)) )
            # Trier les résultats par nombre d'occurrences décroissantes
            sermons = sermons.order_by('-num_occurrences')
            context['query']=query
            if query!= '':
                context['isSearch']=True
            context['sermon']=sermons.filter(show=True)


            # sermon=models.Sermon.objects.all
            # context['sermon']=sermon

    return render(request,'home/sermons.html',context)

def bay(request):
    # fund=models.fundRaiser.objects.filter(show=True).exclude(title="primary").order_by('startupDate')
    # fund2=fund[::-1]
    # fund2=fund2[:5]
    bay=models.bay.objects.get(show=True)
    context={'bay':bay,
            #  'fund':fund2
             }
    return render(request,'home/bay copy.html',context)

def baylibre(request,slug):
    purpose='true'
    try:
        purpose=models.fundRaiser.objects.get(slug=slug)
    except:
        if slug=='primary':
            purpose=models.fundRaiser.objects.create(title=slug,slug=slug,butArgent=0,endlessFund=True)
        else:
            return render(request,'home/notFound.html')
    give=False
    url="#"
    if request.method=="POST":
        amout=0.00
        ismember=False
        data=json.loads(request.body)
        amout=data['amout']
        name=data['name']
        iss=data['ismember']
        if iss=='True':
            ismember=True
        amout=Decimal(amout)
        #amout2=float(amout)
        models.participation.objects.create(name=name,montant=amout,purpose_id=purpose.id,isMember=ismember)
        give=True
        #url=utils.moncashPayment('45789',amout2)
        #print(url)
        return redirect('/home/') 
    bay=models.bay.objects.get(show=True) 
    context={'bay':bay,'give':give,'url':url,'x':purpose}
    return render(request,'home/baylibre.html',context)

def departement(request,slug):
    d=models.secteur.objects.get(slug=slug)
    events=d.events
    context={'departement':d,'event':events}
    return render(request,'home/departement.html',context)


def fundraisers(request):
    fund=models.fundRaiser.objects.filter(show=True).exclude(title="primary").filter(endlessFund=True)
    fund2=models.fundRaiser.objects.filter(show=True).exclude(title="primary").filter(endlessFund=False)
    bay=models.bay.objects.get(show=True)
    context={'bay':bay,'fund1':fund,'fund2':fund2}
    return render(request,'home/fundraisers.html',context)

def articles(request,slug):
    tags=models.tag.objects.all()
       
    context={'tags':tags}

    # sermon=models.Sermon.objects.all
    # tags=models.tag.objects.all()
    Sermons_main_section=models.Sermons_main_section.objects.get(show=True)
    context['page']=Sermons_main_section
    try:
        articleJ=models.article.objects.get(slug=slug)
        relatedarticle=utils.matchesarticle(articleJ)['list']
        # sermon=models.Sermon.objects.all().exclude(title=sermonJ)
        context['articleJ']=articleJ
        context['list']=relatedarticle
    except:
        try:
            slug=slug[:-2]
            slugTest=models.tag.objects.get(title=slug)
            xx=utils.matchOnearticle(slug)
            context['articles']=xx
            context['tag']=slug
           
        except:
            query = request.GET.get('q', '')  # Récupérez le terme de recherche de la requête GET
            # Effectuez une recherche dans les champs désirés
            articles = models.article.objects.filter(
                Q(title__icontains=query) |  # Recherche dans le titre (insensible à la casse)
                Q(sous_titre__icontains=query) |  # Recherche dans le sous-titre (insensible à la casse)
                Q(autor__icontains=query) |  # Recherche dans l'auteur (insensible à la casse)
                Q(paragraphs__icontains=query) |  # Recherche dans le contenu (insensible à la casse)
                Q(tags__title__icontains=query)  # Recherche dans les tags (insensible à la casse)
            )

            # Annoter les résultats avec le nombre d'occurrences du terme de recherche
            articles = articles.annotate(num_occurrences=Count(
                'title', filter=Q(title__icontains=query)) +
                Count('sous_titre', filter=Q(sous_titre__icontains=query)) +
                Count('autor', filter=Q(autor__icontains=query)) +
                Count('paragraphs', filter=Q(paragraphs__icontains=query)) +
                Count('tags', filter=Q(tags__title__icontains=query)) )
            # Trier les résultats par nombre d'occurrences décroissantes
            articles = articles.order_by('-num_occurrences')
            context['query']=query
            if query!='':
                context['isSearch']=True
            context['articles']=articles.filter(show=True)

    return render(request,'home/articles.html',context)