from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.

def home(request):
    slideImages=MainBannerImages.objects.all()
    packages=Packages.objects.all()
    fleets=OurFleets.objects.all()
    blogs=Blog.objects.all()[:3]
    context={
        "slideImages":slideImages,
        "packages":packages,
        "fleets":fleets,
        "blogs":blogs
    }
    return render(request,'index.html',context)



def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def destinations_details(request,slug):
    package=Packages.objects.get(slug=slug)
    events=package.events_set.all()

    packages=Packages.objects.all().exclude(slug=slug)
    context={
        "package":package,
        "events":events,
        "packages":packages


    }
    return render(request,'destination_details.html',context)


def travel_destination(request):
    return render(request,'travel_destination.html')

def blog(request):
    blogs=Blog.objects.all()
    context={
        "blogs":blogs

    }
    return render(request,'blog.html',context)


def blogdetails(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    context = {
        "blog" : blog, 
    }
    return render(request,'single-blog.html',context)