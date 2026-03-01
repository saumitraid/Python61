from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='cont-page'),
    path('add-std', views.add_student, name='add-std'),
]
