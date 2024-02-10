# name is for dynamic urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# include()
#function to connect our app to the entire project
        


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('', include('base.urls')),
    path('inbox/', include('conversation.urls')),
    path('dashboard', include('dashboard.urls')), 
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)