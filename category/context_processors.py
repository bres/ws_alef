from .models import Category

def menu_links(request):
    links = Category.objects.all().exclude(category_name='default').order_by("sort_number")
    return dict(links=links)


def default_link(request):
    categories=Category.objects.filter(category_name="default")
    return dict(categories=categories)