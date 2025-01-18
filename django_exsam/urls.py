from django.urls import path

from django_exsam.views import name

app_name = 'name'

urlpatterns = [
    path('', name, name='list'),
]


