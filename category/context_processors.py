from .models import Category,HeroImages,VideoBannerFront,VideoBannerInside

def menu_links(request):
    links = Category.objects.all().exclude(category_name='default').order_by("sort_number")
    return dict(links=links)


def default_link(request):
    categories=Category.objects.filter(category_name="default")
    return dict(categories=categories)


def default_hero(request):
    heros=HeroImages.objects.all().order_by("hero_number")
    return dict(heros=heros)


def front_banner(request):
    front=VideoBannerFront.objects.all()
    return dict(front=front)


def inside_banner(request):
    inside=VideoBannerInside.objects.all()
    return dict(inside=inside)