# from audioop import add
#
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Permission
# from django.shortcuts import render, redirect
#
# from users.forms import RegistrationForm, LoginForm
#
#
# def registration_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('users:profile')
#
#
#         add.permission = Permission.objects.get(codename='add_booknodel', content_type_app_label='books')
#         change_permission = Permission.objects
#
#
#     else:
#         form = RegistrationForm()
#
#     return render(request, 'registration.html', {'form': form})
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#
#             user = authenticate(request, username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('users:profile')
#     else:
#         form = LoginForm()
#
#     return render(request, 'login.html', {'form': form})
#
#
# @login_required
# def profile_view(request):
#     return render(request, 'profile.html', {'user': request.user})
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('users:login')
def some_view():
    return None