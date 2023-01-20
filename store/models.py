from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    short_desc      = models.TextField(max_length=200, blank=True)
    length          = models.CharField(max_length=50, blank=True)
    height          = models.CharField(max_length=50, blank=True)
    depth           = models.CharField(max_length=50, blank=True)
    weight          = models.CharField(max_length=50, blank=True)
    composition     = models.TextField(max_length=500, blank=True)
    care            = models.TextField(max_length=500, blank=True)
    length_strap    = models.TextField(max_length=50, blank=True)
    handle          = models.TextField(max_length=50, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='images/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    code            =models.CharField(max_length=30,unique=True)
    discount_percentage=models.IntegerField(blank=True,default=0)

    def get_sale(self):
        price = self.price * (100 - self.discount_percentage) / 100
        return price

    def get_url(self):
        return reverse('store:product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    def hardwares(self):
        return super(VariationManager, self).filter(variation_category='hardware', is_active=True)

    def straps(self):
        return super(VariationManager, self).filter(variation_category='strap', is_active=True)

variation_category_choice=(
    ('hardware','hardware'),
    ('strap','strap'),
)

class Variation(models.Model):
    product           =models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variation_category_choice)
    variation_value   =models.CharField(max_length=100)
    is_active         =models.BooleanField(default=True)
    created_date      =models.DateTimeField(auto_now=True)

    objects= VariationManager()

    def __str__(self):
        return self.variation_value



class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'