from django.contrib import admin
from django.urls import path
from . import views
from .views import cosa_per_fare
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('contatti/', views.contact, name="contact"),
    path('galleria/', views.galeria, name="galeria"),
    path('che-siamo/', views.about, name="about"),
    path('cosa-per-fare/', views.cosa_per_fare, name="cosa-per-fare"),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)