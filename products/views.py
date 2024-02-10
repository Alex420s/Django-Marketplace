from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .forms import NewItemForm, EditItemForm
from .models import Product, Category
 
def items(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    query = request.GET.get('query','')
    items = Product.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id= category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'products/items.html',
                  {'items': items, 
                   'query': query,
                   'categories': categories,
                   'category_id': int(category_id)
                   })
# Create your views here.
def detail( request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category, is_sold = False).exclude(pk=pk)[0:3]
    context =  {
        'product': product,
        'related_products': related_products,
        }
    return render(request,'products/detail.html',context=context)

# Only if is_authenticated
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # save form data and adds created_by field afther 
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('products:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'products/form.html', {
        'form': form, 'title': 'New item',
        })
@login_required
def edit(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()

            return redirect('products:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'products/form.html', {
        'form': form, 'title': 'Edit item',
        })

@login_required
def delete( request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    item.delete()
#

    return redirect('dashboard:index') 
    