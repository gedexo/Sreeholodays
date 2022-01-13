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
        "packages":packages,
        "is_post":False,
    }
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        context["is_post"]=True
        context["name"]=name
        context["phone"]=phone

        messageLink="https://wa.me/+919995565129?text=Hey%20I'm%20interested%20in%20your%20following%20package%20"
        messageLink+="%0aPackage%20:"+package.place
        messageLink+="%0aDays%20:"+str(package.days)
        messageLink+="%0aDistrict%20:"+package.district+","+package.state
        messageLink+="%0a"
        messageLink+="%0a"
        messageLink+="%0aName%20:"+name
        messageLink+="%0aPhone%20:"+phone
        context["messageLink"]=messageLink
        return render(request,'destination_details.html',context)


    return render(request,'destination_details.html',context)


def travel_destination(request):

    packages=Packages.objects.all()
    context={
        "packages":packages
    }


    return render(request,'travel_destination.html',context)

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


def bookfleet(request,id):

    fleet=OurFleets.objects.get(id=id)
    context={
        "fleet":fleet,
        "booking":False
    }
    
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        date=request.POST['date']
        context["booking"]=True
        context["name"]=name
        context["phone"]=phone
        context["date"]=date
        messageLink="https://wa.me/+919995565129?text=Hey%20I%20Would%20in%20like%20to%20avail%20your%20following%20service"
        messageLink+="%0a"
        messageLink+="%0a"
        messageLink+="Service%20:"+fleet.name
        messageLink+="%0a"
        messageLink+="Date%20:"+date
        messageLink+="%0a"
        messageLink+="%0a"
        messageLink+="Name%20:"+name
        messageLink+="%0a"
        messageLink+="Phone%20:"+phone
        context["messageLink"]=messageLink

    
    return render(request,"bookfleet.html",context)