from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.

def home(request):
    slideImages=MainBannerImages.objects.all()
    packages=Packages.objects.filter(display_in_home=True)
    fleets=OurFleets.objects.all()
    blogs=Blog.objects.filter(display_in_home=True)
    testimonials=Testimonial.objects.all()
    context={
        "slideImages":slideImages,
        "packages":packages,
        "fleets":fleets,
        "blogs":blogs,
        "testimonials":testimonials
    }
    if request.POST:
       wherego= request.POST['wherego']
       name= request.POST['name']
       dateofJ= request.POST['dateof']
       context["wherego"]=wherego
       context["name"]=name
       context["dateofJ"]=dateofJ
       package=Packages.objects.filter(place=wherego)
       messageLink="https://wa.me/918304948399?text=Hey%20I%20want%20to%20know%20about%20good%20package%20for%20visit%20following%20place"
       messageLink+="%0a"
       messageLink+="Name%20:"+name

       if package.exists():
           context["package"]=package.first()
           messageLink+="%0a"
           messageLink+="Going%20to%20:"+package.first().place
           messageLink+="%0a"
           messageLink+="Distict%20:"+package.first().district
       else:
           messageLink+="Going%20to%20:"+wherego
           
       messageLink+="%0a"
       messageLink+="Date%20:"+dateofJ
       context["messageLink"]=messageLink
       return render(request,'journyenquiry.html',context)

       
    return render(request,'index.html',context)



def about(request):
    testimonials=Testimonial.objects.all()
    blogs=Blog.objects.all()[:3]
    context={
        "testimonials":testimonials,
        "blogs":blogs
        }
    return render(request,'about.html',context)


def contact(request):
    blogs=Blog.objects.all()[:3]
    context={
        "blogs":blogs,
    }

    return render(request,'contact.html',context)


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

        messageLink="https://wa.me/918304948399?text=Hey%20I'm%20interested%20in%20your%20following%20package%20"
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
    blogs=Blog.objects.all()[:3]
    context={
        "packages":packages,
        "blogs":blogs
    }
    if request.POST:
       wherego= request.POST['wherego']
       name= request.POST['name']
       dateofJ= request.POST['dateof']
       context["wherego"]=wherego
       context["name"]=name
       context["dateofJ"]=dateofJ
       package=Packages.objects.filter(place=wherego)
       messageLink="https://wa.me/918304948399?text=Hey%20I%20want%20to%20know%20about%20good%20package%20for%20visit%20following%20place"
       messageLink+="%0a"
       messageLink+="Name%20:"+name

       if package.exists():
           context["package"]=package.first()
           messageLink+="%0a"
           messageLink+="Going%20to%20:"+package.first().place
           messageLink+="%0a"
           messageLink+="Distict%20:"+package.first().district
       else:
           messageLink+="Going%20to%20:"+wherego
           
       messageLink+="%0a"
       messageLink+="Date%20:"+dateofJ
       context["messageLink"]=messageLink
       return render(request,'journyenquiry.html',context)


    return render(request,'travel_destination.html',context)

def blog(request):
    blogs=Blog.objects.all()
    context={
        "blogs":blogs

    }
    return render(request,'blog.html',context)


def blogdetails(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    recentblogs=Blog.objects.all().exclude(slug=slug)
    context = {
        "blog" : blog,
        "recentblogs":recentblogs
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
        Jfrom=request.POST['from']
        Jto=request.POST['to']
        date=request.POST['date']
        context["booking"]=True
        context["name"]=name
        context["phone"]=phone
        context["date"]=date
        messageLink="https://wa.me/918304948399?text=Hey%20I%20Would%20like%20to%20avail%20your%20following%20service"
        messageLink+="%0a"
        messageLink+="%0a"
        messageLink+="Service%20:"+fleet.name
        messageLink+="%0a"
        messageLink+="From%20:"+Jfrom
        messageLink+="%0a"
        messageLink+="To%20:"+Jto
        messageLink+="%0a"
        messageLink+="Date%20:"+date
        messageLink+="%0a"
        messageLink+="%0a"
        messageLink+="Name%20:"+name
        messageLink+="%0a"
        messageLink+="Phone%20:"+phone
        context["messageLink"]=messageLink
        context["from"]=Jfrom
        context["to"]=Jto

    
    return render(request,"bookfleet.html",context)