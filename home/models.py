from pickle import FALSE, TRUE
from pyexpat import model
from re import M
from tkinter import CASCADE
from django.db import models

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
    name= models.CharField(max_length=50,unique=True)
    slug= models.SlugField(unique=True)
    imageBackground=models.FileField(null=True, upload_to='media/images/%y')
    description_bref=models.TextField()
    description= models.TextField()
    horraire=models.CharField(max_length=15)
    show= models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.show== True:
            self.show= False
            try:
                heros= serviceSingle.objects.get(show=True)
                heros.show=False
                heros.save()
            except:
                pass
            self.show=True

        super(serviceSingle, self).save(*args, **kwargs)

class Service(models.Model):
    title=models.CharField(max_length=30, default="Services")
    submenu=models.TextField(default="Nos horraires nous permettent de vous offrir une large evantaille de possibilitee pour vous de nous assister")    
    show=models.BooleanField(default=True)

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
    title= models.CharField(max_length=30)
    orator=models.CharField(max_length=20)
    tumbnail= models.FileField(upload_to='media/images/%y')
    youtubeurl=models.TextField()

class Sermons_main_section(models.Model):
    title=models.CharField(max_length=30, default="Nos Sermons")
    submenu=models.TextField(default="Profitez de nos Sermons")
    show=models.BooleanField(default=True)
    s1= models.ForeignKey(Sermon,on_delete=models.CASCADE,related_name='s1')
    s2= models.ForeignKey(Sermon,on_delete=models.CASCADE,related_name='s2')
    s3= models.ForeignKey(Sermon,on_delete=models.CASCADE,related_name='s3')

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
    ref=models.CharField(max_length=15)
    verset= models.TextField()

class verset_main_page(models.Model):
    theme= models.CharField(max_length=50)
    v1=models.ForeignKey(verset,on_delete=models.CASCADE,related_name='v1')
    v2=models.ForeignKey(verset,on_delete=models.CASCADE,related_name='v2')
    v3=models.ForeignKey(verset,on_delete=models.CASCADE,related_name='v3')
    show=models.BooleanField(default=True)

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

class evenement(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    startdate=models.DurationField()
    description=models.TextField(null=True)

class evenement_main_page(models.Model):
    title=models.CharField(max_length=30)
    subtitle=models.TextField()
    e1=models.ForeignKey(evenement,on_delete=models.CASCADE,related_name='e1')
    e2=models.ForeignKey(evenement,on_delete=models.CASCADE,related_name='e2')
    e3=models.ForeignKey(evenement,on_delete=models.CASCADE,related_name='e3')
    show=models.BooleanField(default=True)

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
    title=models.CharField(max_length=30,default="Nos Secteurs")
    subtitle=models.TextField()
    show=models.BooleanField(default=True)

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
    title=models.CharField(max_length=40,null=True,blank=True)
    description= models.TextField(null=True,blank=True,default= 'this is the default populated description')
    slug=models.SlugField(null=True,blank=True,default= 'this is the default populated slug')
    tumbail= models.FileField(null=True,blank=True)
    titit= models.CharField(max_length=50,null=True,blank=True)