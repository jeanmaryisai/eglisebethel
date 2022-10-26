from django import views
from django.urls import path
from . import views

urlpatterns = [path('', views.home, name='home'),
                path('about', views.about, name='about'),
                path('events', views.events, name='events'),
                path('singlevents/<slug:slug>', views.singlevents, name='singlevents'),
                path('sermons/<slug:slug>', views.sermons, name='sermons'),
                path('bay', views.bay, name='bay'),
                # path('secteur/<slug:slug>', views.secteur, name='secteur'),
                path('baylibre/<slug:slug>', views.baylibre, name='baylibre'),
                path('contact', views.contact, name='contact'),
                path('fundraisers', views.fundraisers, name='fundraisers'),
                path('story', views.story, name='story'),

]