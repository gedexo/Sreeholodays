from statistics import mode
from django.db import models
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from django.db.models.fields import BLANK_CHOICE_DASH
from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.
from tinymce.models import HTMLField

class MainBannerImages(models.Model):
    image = VersatileImageField(upload_to = 'bannerimages',ppoi_field='image_ppoi',blank=True)
    image_ppoi = PPOIField()
    
    





class Packages(models.Model):
    place=models.CharField(max_length=225)
    district=models.CharField(max_length=225,null=True,blank=True)
    state=models.CharField(max_length=225,null=True,blank=True)
    slug=models.SlugField(unique=True)
    image=VersatileImageField(upload_to = 'packages',ppoi_field='image_ppoi',blank=True)
    image_ppoi = PPOIField()
    days=models.IntegerField(null=True,blank=True)
    price =models.IntegerField(null=True,blank=True)
    shortdiscription=models.TextField(blank=True,null=True)
    discription_heading=models.CharField(max_length=225,null=True,blank=True)
    discription=HTMLField(blank=True,null=True)
    display_in_home=models.BooleanField(default=True)

    def __str__(self):
        return str(self.place)
    


class Events(models.Model):
    package=models.ForeignKey(Packages,on_delete=models.CASCADE)
    eventHead=models.CharField(max_length=225,null=True,blank=True)
    image=VersatileImageField(upload_to = 'events',ppoi_field='image_ppoi',null=True,blank=True)
    image_ppoi = PPOIField()
    shortdiscription=HTMLField(blank=True,null=True)

    def __str__(self):
        return str(self.package)
    


class Blog(models.Model):
    bloghead=models.CharField(max_length=225)
    image=VersatileImageField(upload_to = 'blog',ppoi_field='image_ppoi',null=True,blank=True)
    image_ppoi = PPOIField()
    month=models.CharField(max_length=225,blank=True,null=True)
    day=models.CharField(max_length=225,blank=True,null=True)
    year=models.CharField(max_length=225,blank=True,null=True)
    description=HTMLField(blank=True,null=True)
    slug = models.SlugField()
    display_in_home=models.BooleanField(default=True)

    def __str__(self):
        return str(self.bloghead)


class OurFleets(models.Model):
    name=models.CharField(max_length=225)
    image=VersatileImageField(upload_to = 'fleets',ppoi_field='image_ppoi',null=True,blank=True)
    image_ppoi = PPOIField()
    image_two=VersatileImageField(upload_to = 'fleets',ppoi_field='image_two_ppoi',null=True,blank=True)
    image_two_ppoi = PPOIField()
    image_three=VersatileImageField(upload_to = 'fleets',ppoi_field='image_three_ppoi',null=True,blank=True)
    image_three_ppoi = PPOIField()

    image_four=VersatileImageField(upload_to = 'fleets',ppoi_field='image_four_ppoi',null=True,blank=True)
    image_four_ppoi = PPOIField()
    seats=models.CharField(max_length=225)

    def __str__(self):
        return str(self.name)

    

class Testimonial(models.Model):
    image=VersatileImageField(upload_to = 'testimonial',ppoi_field='image_ppoi',null=True,blank=True)
    image_ppoi = PPOIField()
    name=models.CharField(max_length=225,blank=True,null=True)
    message=HTMLField()

