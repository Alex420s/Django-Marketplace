from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.index , name='index'),
    path('signup/', views.signup, name='signup'),
]
