from django.shortcuts import render

def index(request):
    return render(request, 'content/index.html')

def contact(request):
    return render(request, 'content/contact.html')