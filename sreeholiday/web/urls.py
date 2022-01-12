
from django.urls import path
from .views import *
app_name='web'
urlpatterns = [
    path('', home,name="home"),
    path('about/', about,name="about"),
    path('contact/', contact,name="contact"),
    path('destination/<str:slug>/', destinations_details,name="destination"),
    path('destinations/', travel_destination,name="destinations"),
    path('blog/', blog,name="blog"),
    path('blogdetails/<str:slug>/', blogdetails,name="blogdetails"),
]
