from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='cont-page'),
    path('add-std', views.add_student, name='add-std'),
    path('view-std', views.viewStudent, name='view-std'),
    path('std-delete',views.delStudent ,name='std-delete'),
]
