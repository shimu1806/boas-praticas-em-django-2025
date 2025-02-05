from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contatti/', views.contact, name="contact"),
    path('galleria/', views.galeria, name="galeria"),
    path('che-siamo/', views.about, name="about"),
]