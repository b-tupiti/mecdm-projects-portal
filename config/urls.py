from django.contrib import admin
from django.urls import path, include
from users.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('requests/', include('requests.urls')),
    path('projects/', include('projects.urls')),
    
    # temporary
    path('', home, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
