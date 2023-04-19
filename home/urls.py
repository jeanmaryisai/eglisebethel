from django import views
from django.urls import path
from .views import *

urlpatterns = [path('home/', home, name='home'),
                path('home/about', about, name='about'),
                path('home/events', events, name='events'),
                path('home/singlevents/<slug:slug>', singlevents, name='singlevents'),
                path('home/sermons/<slug:slug>', sermons, name='sermons'),
                path('home/bay', bay, name='bay'),
                path('home/baylibre/<slug:slug>', baylibre, name='baylibre'),
                path('home/contact',contact, name='contact'),
                path('home/fundraisers',fundraisers, name='fundraisers'),
                path('home/departement/<slug:slug>', departement, name='departement'),
                path('home/articles/<slug>',articles, name='articles'),
]