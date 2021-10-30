from django.shortcuts import get_object_or_404,render,redirect,HttpResponse
from django.contrib.auth.decorators import  login_required
from .models import Product
from category.models import Category
from .forms import ProductForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/detail.html',
                  {'product': product})



@login_required
def create_product(request):
    if request.user.is_superuser:
        form=ProductForm()
        if request.method == 'POST':
            form = ProductForm(request.POST,request.FILES)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.created_by=request.user
                instance.save()
                return redirect('shop:product_list')
        context ={
          "form":form
        }
        return render(request, 'shop/create.html', context )
    else:
        return HttpResponse('You are not allowed to be here!')


def update_product(request, slug):
    if request.user.is_superuser:
        product = get_object_or_404(Product, slug=slug)
        if request.method == "POST":
            form = ProductForm(request.POST,request.FILES,instance=product)
            if form.is_valid():
                form.save()
                return redirect('shop:product_list')
        else:
            form = ProductForm(instance=product)
        context ={
            "form":form
            }
        return render(request, 'shop/update.html', context)
    else:
        return HttpResponse('You are not allowed to be here!')


def delete_product(request, slug):
    if request.user.is_superuser:
        product=Product.objects.get(slug=slug)
        if request.method == 'POST':
            product.delete()
            return redirect('shop:product_list')
        return render(request,'shop/delete.html',{'obj':product })
    else:
        return HttpResponse('You are not allowed to be here!')