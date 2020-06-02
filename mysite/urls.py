from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
]
