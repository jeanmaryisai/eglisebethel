from django import views
from django.urls import path
from . import views

urlpatterns = [path('home/', views.home, name='home'),
                path('home/about', views.about, name='about'),
                path('home/events', views.events, name='events'),
                path('home/contact', views.sermons, name='sermons'),
                path('home/bay', views.bay, name='bay'),
                
]