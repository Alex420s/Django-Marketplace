# name is for dynamic urls
from django.contrib import admin
from django.urls import path
from base.views import index, contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact', contact, name='contact'),
    path('', index , name='index'),
]
