from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('tinymce/', include('tinymce.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




admin.site.site_header = "SREE HOLIDAYS Administration"
admin.site.site_title = "SREE HOLIDAYS Admin Portal"
admin.site.index_title = "Welcome to SREE HOLIDAYS Admin Portal"
