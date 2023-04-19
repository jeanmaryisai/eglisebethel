
import moncashify
from . import models

def moncashPayment(id,money):
    client_id='5963fcd6da676836aa985d13ee53bef7'
    secret_key='oHrr4tbnB1PH0uz6VQNUvbvyBM0aiLPgBxVs22tJEj22zoHrURKFvjBykwveAFIr'
    moncash=moncashify.API(client_id, secret_key, debug=True)
    payment = moncash.payment(id, money)
    url=payment.get_redirect_url()
    return url

def ev(n):
    evenement=models.evenement.objects.filter(show=True).order_by('startdate')
    e=evenement[::-1]
    n=n-1
    try:
        return e[n]
    except:
        return False
def matches(sermon):
    sermons=models.Sermon.objects.all().exclude(title=sermon.title)
    tag=sermon.tags.all()
    tage=[]
    for x in tag:
        tage.append(x.title)
    matches={}
    for x in sermons:
        ma=0
        for y in x.tags.all():
            if y.title in tage:
                ma =ma +1
        if ma>0:        
            matches[x.title]=ma
    sortedmatches=dict(sorted(matches.items(),key=lambda item:item[1],reverse=True))

    lis=list(sortedmatches.keys())
    li=[]
    for x in lis:
        li.append(models.Sermon.objects.get(title=x))
    return {'list':li,'dict':sortedmatches}

def matchOne(tag):
    sermons=models.Sermon.objects.all()
    sermon=[]
    
    for x in sermons:
        tage=[]
        for y in x.tags.all():
            tage.append(y.title)
        if tag in tage:
            sermon.append(x)
    return sermon

def matchOnearticle(tag):
    sermons=models.article.objects.all()
    sermon=[]
    
    for x in sermons:
        tage=[]
        for y in x.tags.all():
            tage.append(y.title)
        if tag in tage:
            sermon.append(x)
    return sermon

def matchesarticle(article):
    sermons=models.article.objects.all().exclude(slug=article.slug)
    tag=article.tags.all()
    tage=[]
    for x in tag:
        tage.append(x.title)

    matches={}
    for x in sermons:
        ma=0
        for y in x.tags.all():
            if y.title in tage:
                ma =ma +1
        if ma>0:        
            matches[x.title]=ma
    sortedmatches=dict(sorted(matches.items(),key=lambda item:item[1],reverse=True))

    lis=list(sortedmatches.keys())
    li=[]
    for x in lis:
        li.append(models.article.objects.get(title=x))
    return {'list':li,'dict':sortedmatches}