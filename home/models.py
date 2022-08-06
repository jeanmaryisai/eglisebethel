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
    backgroud=models.ImageField(null=True, upload_to='images/%y')
    video=models.FileField(null=True, upload_to='videos/%y')
    def __str__ (self):
        return self.name

class hero(models.Model):
    name=models.CharField(max_length= 40)
    vid1=models.ForeignKey(heroSingle,on_delete=models.CASCADE,related_name='vid1')
    vid2=models.ForeignKey(heroSingle,on_delete=models.CASCADE,related_name='vid2')
    vid3=models.ForeignKey(heroSingle,on_delete=models.CASCADE,related_name='vid3')
    show= models.BooleanField()
    def __str__ (self):
        return self.name

   
    

