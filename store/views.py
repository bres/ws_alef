from django.shortcuts import get_object_or_404,render,redirect,HttpResponse
from django.contrib.auth.decorators import  login_required
from .models import Category,Product
from .forms import ProductForm
# Create your views here.


def categories(request):
      return {
           'categories':Category.objects.all()
      }

def all_products(request):
     products=Product.objects.all()
     return render(request,'store/products.html',{'products':products})

def product_detail(request,slug):
     product = get_object_or_404(Product ,slug=slug ,in_stock=True)
     return render(request,'store/detail.html',{'product':product})

def category_list(request, category_slug):
     category = get_object_or_404(Category ,slug=category_slug)
     products = Product.objects.filter(category=category)
     return render(request,'store/category.html',{'category':category,'products':products})


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
                return redirect('store:all_products')
        context ={
          "form":form
        }
        return render(request, 'store/create.html', context )
    else:
        return HttpResponse('You are not allowed to be here!')


def update_product(request, slug):
    if request.user.is_superuser:
        product = get_object_or_404(Product, slug=slug)
        if request.method == "POST":
            form = ProductForm(request.POST,request.FILES,instance=product)
            if form.is_valid():
                form.save()
                return redirect('store:all_products')
        else:
            form = ProductForm(instance=product)
        context ={
            "form":form
            }
        return render(request, 'store/update.html', context)
    else:
        return HttpResponse('You are not allowed to be here!')


def delete_product(request, slug):
    if request.user.is_superuser:
        product=Product.objects.get(slug=slug)
        if request.method == 'POST':
            product.delete()
            return redirect('store:all_products')
        return render(request,'store/delete.html',{'obj':product })
    else:
        return HttpResponse('You are not allowed to be here!')
