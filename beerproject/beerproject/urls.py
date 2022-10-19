from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from beer.views import index
from django.urls import path, include
from beerproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('beer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)