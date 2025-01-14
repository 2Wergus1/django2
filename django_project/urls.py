from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from . import views

urlpatterns = [
    path('email/', views.email, name='email'),
    path('phone_number/', views.phone_number, name='phone_number'),
    path('hobby/', views.hobby, name='hobby'),
]
