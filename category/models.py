from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=255,blank=True)
    image = models.ImageField(upload_to='images/categories', blank=True)
    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])