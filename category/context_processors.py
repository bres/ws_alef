from .models import Category

def menu_links(request):
    links = Category.objects.all().exclude(category_name='default')
    return dict(links=links)


def gallery_links(request):
    gallery_links = Category.objects.all().exclude(category_name='default').exclude(category_name='all products').order_by("sort_number")
    return dict(gallery_links=gallery_links)



def default_link(request):
    
    categories=Category.objects.filter(category_name="default")
    
    return dict(categories=categories)