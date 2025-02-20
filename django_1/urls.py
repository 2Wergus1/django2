from django.urls import path
from .views import ProductView, RegisterView, LoginView, LogoutView

app_name = 'django_1'

urlpatterns = [
    path('products/', ProductView.as_view(), name='product_list'),
    path('products/<int:product_id>/', ProductView.as_view(), name='product_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
