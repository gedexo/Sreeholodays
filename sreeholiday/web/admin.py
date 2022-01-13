from django.contrib import admin
from .models import *
# Register your models here.


class EventInline(admin.TabularInline):
    model=Events
    extra=2

class PackagesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('place',)}
    inlines=[EventInline]
    list_display = ('place', 'days', 'shortdiscription')

admin.site.register(MainBannerImages)

class EventsAdmin(admin.ModelAdmin):
    list_display = ('package', 'eventHead', 'shortdiscription')

class OurFleetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'seats',)

admin.site.register(Packages,PackagesAdmin)
admin.site.register(Events,EventsAdmin)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('bloghead',)}
    list_display = ('bloghead',)
admin.site.register(Blog,BlogAdmin)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'message',)
admin.site.register(Testimonial,TestimonialAdmin)

admin.site.register(OurFleets,OurFleetsAdmin)
