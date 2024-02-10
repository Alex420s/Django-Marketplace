from django.shortcuts import render, redirect

from products.models import Category, Product
from .forms import SignupForm

def index(request):
    productos = Product.objects.filter(is_sold=False)[0:6]
    categorias = Category.objects.all()
    context = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'base/index.html', context=context)

def contact(request):
    return render(request, 'base/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard:index')
    else:
        form = SignupForm()

    return render(request, 'base/signup.html', {'form':form})