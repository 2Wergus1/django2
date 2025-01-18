from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_exsam.urls', namespace='django_exsam'))
]

