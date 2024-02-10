from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404

from products.models import Product

@login_required
def index(request):
    items = Product.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'productos': items,
    })

