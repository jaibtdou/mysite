from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('polls/', include('polls.urls')),
    path('chat/', include('chat.urls')),
]
