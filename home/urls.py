from django import views
from django.urls import path
from . import views

urlpatterns = [path('home/', views.home, name='home'),
                path('home/about', views.about, name='about'),
                path('home/events', views.events, name='events'),
                path('home/sermons', views.sermons, name='sermons'),
                path('home/bay', views.bay, name='bay'),
                 path('home/baylibre', views.baylibre, name='baylibre'),
                path('home/contact', views.contact, name='contact'),
                
]