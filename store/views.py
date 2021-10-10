from django.shortcuts import get_object_or_404,render,redirect
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

def create_product(request):
    form=ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.user=request.user
            product.save()
            #form.save()
            return redirect('store:all_products')
    context ={
      "form":form
    }
    return render(request, 'store/create.html', context )



 
def update_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    context ={
        "form":form
        }
    return render(request, 'store/update.html', context)
 
 
def delete_product(request, slug):
    product=Product.objects.get(slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('store:all_products')
    return render(request,'store/delete.html',{'obj':product })

