from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('destinations/', destinations, name='destination'),
    path('detail/<int:id>/', detail, name='detail'),
]
