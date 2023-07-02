# name is for dynamic urls
from django.conf import settings
from django.contrib import admin
from django.urls import path
from base.views import index, contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact', contact, name='contact'),
    path('', index , name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)