from django.urls import path

from books.views import template_view,book_detail

app_name = 'books'

urlpatterns = [
    path('', template_view, name='list'),
    path('<int:pk>/detail', book_detail, name='detail')
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('first_name/', views.first_name, name='first_name'),
    path('last_name/', views.last_name, name='last_name'),
]
