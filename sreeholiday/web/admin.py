from django.contrib import admin
from .models import *
# Register your models here.


class EventInline(admin.TabularInline):
    model=Events
    extra=2

class PackagesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('place',)}
    inlines=[EventInline]
    

admin.site.register(MainBannerImages)



admin.site.register(Packages,PackagesAdmin)
admin.site.register(Events)
admin.site.register(Blog)
admin.site.register(OurFleets)
