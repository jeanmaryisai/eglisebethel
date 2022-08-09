from pickle import FALSE, TRUE
from re import M
from tkinter import CASCADE
from django.db import models

# Create your models here.
class secteur(models.Model):
    name=models.CharField(max_length=240)
    show=models.BooleanField(default=False)
    def __str__ (self):
        return self.name

class heroSingle(models.Model):
    name= models.CharField(max_length=39)
    heading= models.TextField()
    submenu1= models.TextField()
    submenu2= models.CharField(max_length=50)
    backgroud=models.ImageField(null=True, upload_to='media/images/%y')
    video=models.FileField(null=True, upload_to='media/videos/%y')
    def __str__ (self):
        return self.name

class hero(models.Model):
    name=models.CharField(max_length= 40)
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
    main=models.CharField(max_length=100)
    submain= models.TextField()
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
    text=models.TextField()
    sat1Name=models.CharField(max_length=50)
    sat2Name=models.CharField(max_length=50)
    sat3Name=models.CharField(max_length=50)
    sat4Name=models.CharField(max_length=50)
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
    name= models.CharField(max_length=50)
    slug= models.SlugField()
    imageBackground=models.FileField(null=True, upload_to='media/images/%y')
    description_bref=models.TextField()
    description= models.TextField()
    horraire=models.CharField(max_length=15)
    show= models.BooleanField()

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
    title=models.CharField(max_length=30)
    submenu=models.TextField()
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

class Sermons_main_section(models.Model):
    title=models.CharField(max_length=30)
    submenu=models.TextField()
    show=models.BooleanField(default=True)

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

class Sermon(models.Model):
    title= models.CharField(max_length=30)
    orator=models.CharField(max_length=20)
    tumbnail= models.FileField(upload_to='media/images/%y')
    youtubeurl=models.TextField()

class verset(models.Model):
    ref=models.CharField()
    verset= models.TextField()

class verset_main_page(models.Model):
    theme= models.CharField(max_length=50)
    v1=models.ForeignKey(verset)
    v2=models.ForeignKey(verset)
    v3=models.ForeignKey(verset)

class evenement(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    startdate=models.DurationField()
    description=models.TextField()

    def isfinished(self):
        return True
