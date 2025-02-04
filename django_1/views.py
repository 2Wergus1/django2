from django.shortcuts import render

def name(request):
    return render(request,'profile.html')
