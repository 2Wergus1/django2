# from django.shortcuts import render
#
# from books.models import BookModel
#
#
# def template_view(request):
#     books = BookModel.objects.order_by('-pk')
#     context = {
#         'books': books
#     }
#
#     return render(request, 'index.html', context)
#
#
# def book_detail(request, pk):
#     pass


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")

def first_name(request):
    return HttpResponse("Your first name is John.")

def last_name(request):
    return HttpResponse("Your last name is Doe.")


def template_view():
    return None