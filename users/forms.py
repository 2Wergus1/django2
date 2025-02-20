# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#
# from users.models import UserModel
#
#
# class RegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True)
#     last_name = forms.CharField(max_length=30, required=True)
#
#     class Meta:
#         model = UserModel
#         fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
#
#
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=30, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)

users = {}

def register(username, password):
    if username in users:
        return "Bu foydalanuvchi allaqachon mavjud!"
    users[username] = password
    return "Ro‘yxatdan o‘tish muvaffaqiyatli!"

def login(username, password):
    if users.get(username) == password:
        return "Tizimga muvaffaqiyatli kirdingiz!"
    return "Login yoki parol noto‘g‘ri!"

def logout():
    return "Tizimdan chiqdingiz!"

# Misol:
print(register("user1", "1234"))
print(login("user1", "1234"))
print(logout())
