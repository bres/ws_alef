# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='images/categories')
    sort_number=models.CharField(max_length=50,unique=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse('store:products_by_category',
    #                    args=[self.slug])

    def get_url(self):
         return reverse('store:products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name



class HeroImages(models.Model):
    hero_title = models.TextField(max_length=200,blank=True)
    hero_subtitle = models.TextField(max_length=200,blank=True)
    herotitle_position = models.CharField(max_length=50,blank=True)
    herotitle_color = models.CharField(max_length=50,blank=True)
    hero_link_state =models.CharField(max_length=200,default='on')
    hero_link =models.CharField(max_length=200,blank=True)
    hero_link_color = models.CharField(max_length=50,blank=True)
    hero_link_bgcolor = models.CharField(max_length=50,blank=True)
    hero_href =models.CharField(max_length=200,blank=True)
    hero_image = models.ImageField(upload_to='images/heros')
    hero_number = models.CharField(max_length=50, unique=True)
    hero_position=models.CharField(max_length=50,blank=True)



    class Meta:
        verbose_name = 'hero_image'
        verbose_name_plural = 'hero_images'

    def __str__(self):
        return self.hero_title+ " " + self.hero_number


