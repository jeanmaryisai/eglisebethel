
from email.mime import image
from django.db import models
import datetime
import pytz
from django.utils.dateparse import parse_duration

#from datetime import datetime, date, time, timedelta
# Create your models here.

class heroSingle(models.Model):
    name= models.CharField(max_length=39,unique=True)
    heading= models.TextField()
    submenu1= models.TextField()
    submenu2= models.CharField(max_length=50)
    backgroud=models.ImageField(null=True, upload_to='media/images/%y')
    video=models.FileField(null=True, upload_to='media/videos/%y')
    def __str__ (self):
        return self.name

class hero(models.Model):
    name=models.CharField(max_length= 40,unique=True)
    vid1=models.ForeignKey(heroSingle,on_delete=models.CASCADE,related_name='vid1')
    vid2=models.ForeignKey(heroSingle,on_delete=models.CASCADE,related_name='vid2')
    vid3=models.ForeignKey(heroSingle,on_delete=models.CASCADE,related_name='vid3')
    show= models.BooleanField(default= True)
    def __str__ (self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= hero.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True

        super(hero, self).save(*args, **kwargs)   

class firstSection(models.Model):
    main=models.CharField(max_length=100,unique=True, default='Prions sans cesse')
    submain= models.TextField(default="Nous rependons la parole de Dieu qu'importe ou nous allons et nous agissons selon les prescriptions laisser par Jesus Christ")
    show= models.BooleanField(default= True)
    
    
    def __str__ (self):
        return self.main

    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= firstSection.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True

        super(firstSection, self).save(*args, **kwargs) 

class statSection(models.Model):
    text=models.TextField(default="Notres statistique durants les deux dernier annees")
    sat1Name=models.CharField(max_length=50,default='Membres')
    sat2Name=models.CharField(max_length=50,default="Ministeres")
    sat3Name=models.CharField(max_length=50,default="Missions")
    sat4Name=models.CharField(max_length=50,default="Activites")
    sat1=models.IntegerField()
    sat2=models.IntegerField()
    sat3=models.IntegerField()
    sat4=models.IntegerField()
    show= models.BooleanField(default= True)
    anneCourante=models.IntegerField(null=True,blank=True)

    def __str__ (self):
        return f'{self.anneCourante}'

    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= statSection.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True

        super(statSection, self).save(*args, **kwargs)

class serviceSingle(models.Model):
    title= models.CharField(max_length=50,unique=True)
    slug= models.SlugField(unique=True)
    imageBackground=models.FileField(null=True, upload_to='media/images/%y')
    description_bref=models.TextField()
    description= models.TextField()
    horraire=models.CharField(max_length=15)
    show= models.BooleanField(default=True)

    def __str__ (self):
        return self.title


class Service(models.Model):
    title=models.CharField(max_length=30,unique=True, default="Services")
    submenu=models.TextField(default="Nos horraires nous permettent de vous offrir une large evantaille de possibilitee pour vous de nous assister")    
    show=models.BooleanField(default=True)
    def __str__ (self):
        return self.title

    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= Service.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True

        super(Service, self).save(*args, **kwargs)

class Sermon(models.Model):
    title= models.CharField(max_length=30,unique=True)
    orator=models.CharField(max_length=20)
    tumbnail= models.FileField(upload_to='media/images/%y')
    youtubeurl=models.TextField()
    show=models.BooleanField(default=True, null=True)
        

    def __str__ (self):
        return self.title

class Sermons_main_section(models.Model):
    title=models.CharField(max_length=30,unique=True, default="Nos Sermons")
    submenu=models.TextField(default="Profitez de nos Sermons")
    show=models.BooleanField(default=True)
    s1= models.ForeignKey(Sermon,on_delete=models.CASCADE,related_name='s1')
    s2= models.ForeignKey(Sermon,on_delete=models.CASCADE,related_name='s2')
    s3= models.ForeignKey(Sermon,on_delete=models.CASCADE,related_name='s3')
    background=models.FileField(upload_to='media/images/%y', null=True)
    def __str__ (self):
        return self.title
    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= Sermons_main_section.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True
            
        super(Sermons_main_section, self).save(*args, **kwargs)

class verset(models.Model):
    ref=models.CharField(max_length=15,unique=True)
    verset= models.TextField()
    def __str__ (self):
        return self.ref

class verset_main_page(models.Model):
    theme= models.CharField(max_length=50,unique=True)
    v1=models.ForeignKey(verset,on_delete=models.CASCADE,related_name='v1')
    v2=models.ForeignKey(verset,on_delete=models.CASCADE,related_name='v2')
    v3=models.ForeignKey(verset,on_delete=models.CASCADE,related_name='v3')
    show=models.BooleanField(default=True)

    def __str__ (self):
        return self.theme

    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= verset_main_page.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True
            
        super(verset_main_page, self).save(*args, **kwargs)


class Img(models.Model):
    img=models.ImageField(upload_to='media/images/%y')
class evenement(models.Model):
    
    title=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(unique=True, editable=False)
    startdate=models.DateTimeField(null=True)
    description=models.TextField(null=True)
    isprimaray=models.BooleanField(default=False,null=True)
    estimatedDuration=models.DurationField(null=True)
    album=models.ManyToManyField(Img,null=True)
    show=models.BooleanField(default=True)

    @property
    def isExpired(self): 
        utc= pytz.UTC
        dat=datetime.timedelta(days=30)
        d=self.startdate + dat
        t=utc.localize(datetime.datetime.now())
        if(d>=t):
            return True
        return False
    @property
    def Haspassed(self): 
        utc= pytz.UTC
        duration = parse_duration(self.estimatedDuration)

        seconds = duration.seconds
        dat=datetime.timedelta(seconds=seconds)
        d=self.startdate + dat
        t=utc.localize(datetime.datetime.now())
        if(d>=t):
            return True
        return False    

    def __str__(self) -> str:
        return self.title

class evenement_main_page(models.Model):
    title=models.CharField(max_length=30,unique=True)
    subtitle=models.TextField()
    e1=models.ForeignKey(evenement,on_delete=models.CASCADE,related_name='e1')
    e2=models.ForeignKey(evenement,on_delete=models.CASCADE,related_name='e2')
    e3=models.ForeignKey(evenement,on_delete=models.CASCADE,related_name='e3')
    show=models.BooleanField(default=True)
    background=models.FileField(upload_to='media/images/%y', null=True)

    def __str__ (self):
        return self.title

    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= evenement_main_page.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True
            
        super(evenement_main_page, self).save(*args, **kwargs)

class secteur_main(models.Model):
    title=models.CharField(max_length=30,unique=True,default="Nos Secteurs")
    subtitle=models.TextField()
    show=models.BooleanField(default=True)

    def __str__ (self):
        return self.title

    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= secteur_main.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True
            
        super(secteur_main, self).save(*args, **kwargs)

class secteur(models.Model):
    title=models.CharField(max_length=40,null=True,blank=True,unique=True)
    description= models.TextField(null=True,blank=True,unique=True,default= 'this is the default populated description')
    slug=models.SlugField(null=True,blank=True)
    tumbail= models.FileField(null=True ,upload_to='media/images/%y')
    titit= models.CharField(max_length=50,null=True,blank=True)
    show=models.BooleanField(default=True, null=True)
        
    def __str__ (self):
        return self.title

class contact_page(models.Model):
    title=models.CharField(max_length=30, default='standard')
    hero_img= models.FileField(upload_to='media/images/%y')
    title_hero=models.CharField(max_length=30, default='Contactez Nous')
    subtile_hero= models.TextField(default="Laissez nous un message, vos demande de prieres.")
    title=models.CharField(max_length=30, default='Contactez Nous')
    subtile= models.TextField(default="Qu'importe ou vous est dans le monde, la puissance du Seigneur reste et demeur le meme")
    title2=models.CharField(max_length=10, default='Address')
    address=models.CharField(max_length=50, default='Rue Louverture Rebecca prolongee #32')
    telphone=models.CharField(max_length=30, default='+509 43 89 0007')
    email=models.EmailField()
    siteweb=models.CharField(max_length=20)
    show=models.BooleanField(default=True)
    def __str__ (self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= contact_page.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True
            
        super(contact_page, self).save(*args, **kwargs)

class about_page(models.Model):
    title=models.CharField(max_length=30, default='standard')
    hero_img= models.FileField(upload_to='media/images/%y')
    title_hero=models.CharField(max_length=30, default='A propos de nous')
    subtile_hero= models.TextField(default="Nous somme une eglise protestante situe en Haiti")
    show=models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= about_page.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True
            
        super(about_page, self).save(*args, **kwargs)


class li_subtitle_about(models.Model):
    title=models.CharField(max_length=50)
    show=models.BooleanField(default=True, null=True)
        
    def __str__ (self):
        return self.title
    
class wrapper_about_page(models.Model):
    wrapper_about_page=models.ManyToManyField(li_subtitle_about,blank=True)
    title=models.CharField(max_length=100)
    paragraph=models.TextField(null=True)

    def __str__ (self):
        return self.title

class live(evenement):
    link=models.URLField()
    tumnail=models.ImageField(upload_to='media/images/%y',null=True)
    autoclosed=models.BooleanField(default=False, null=True)
   


class bay(models.Model):
    title=models.CharField(default="Standard1",max_length=50)
    title_hero=models.CharField( default="Bay Bondye",max_length=50)
    subtitle_hero= models.TextField(null=True)
    show=models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= bay.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True
            
        super(bay, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.title
