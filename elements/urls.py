from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('contact/', views.Form),
    path('submit/', views.Temp),
    path('abilities/', views.Abilities),
    path('counter-strike/', views.Counter),
    path('healing/', views.Heal),
    path('intelligence/', views.Intel),
    path('recombulation/', views.Recomb),
    path('soulstealing/', views.Soulsteal),
    path('survival/', views.Survive),
]