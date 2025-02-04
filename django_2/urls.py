from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_2 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('django_1.urls', namespace='django_1')),
    path('', include('users.urls', namespace='users')),
]









ъ






































































