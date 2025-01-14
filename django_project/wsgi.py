"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()


from django.shortcuts import render
from django.http import HttpResponse

def email(request):
    return HttpResponse("Your email address is example@example.com.")

def phone_number(request):
    return HttpResponse("Your phone number is +1234567890.")

def hobby(request):
    return HttpResponse("Your hobby is gardening.")
