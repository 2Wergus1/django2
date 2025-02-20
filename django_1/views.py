from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.middleware.csrf import get_token
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from .models import Product

User = get_user_model()


@method_decorator(csrf_exempt, name='dispatch')
class ProductView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        page = int(request.GET.get('page', 1))
        products = Product.objects.all() if request.user.is_staff else Product.objects.filter(user=request.user)

        paginator = Paginator(products, 10)
        page_obj = paginator.get_page(page)

        return JsonResponse({
            'products': list(page_obj.object_list.values()),
            'page': page_obj.number,
            'total_pages': paginator.num_pages
        })

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        try:
            data = json.loads(request.body)
            product = Product.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                price=data.get('price'),
                user=request.user
            )
            return JsonResponse({'id': product.id, 'name': product.name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request, product_id):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        try:
            data = json.loads(request.body)
            product = Product.objects.get(id=product_id)

            if request.user.is_staff or product.user == request.user:
                product.name = data.get('name', product.name)
                product.description = data.get('description', product.description)
                product.price = data.get('price', product.price)
                product.save()
                return JsonResponse({'message': 'Product updated successfully'})
            return JsonResponse({'error': 'Permission denied'}, status=403)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, product_id):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)

        try:
            product = Product.objects.get(id=product_id)

            if request.user.is_staff or product.user == request.user:
                product.delete()
                return JsonResponse({'message': 'Product deleted successfully'})
            return JsonResponse({'error': 'Permission denied'}, status=403)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            return JsonResponse({'message': 'User registered successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return JsonResponse({'message': 'Login successful'})
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})
