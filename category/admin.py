from django.contrib import admin
from .models import Category,HeroImages,VideoBannerFront,VideoBannerInside


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','slug')


class HeroImagesAdmin(admin.ModelAdmin):
        prepopulated_fields = {'hero_title': ('hero_number',)}

        list_display = ('hero_number','hero_title',)

    # prepopulated_fields = {'hero_title': ('hero_image',)}
    # list_display = ('hero_image','hero_title')

class VideoBannerFrontAdmin(admin.ModelAdmin):
    list_display = ('video_title',)
class VideoBannerInsideAdmin(admin.ModelAdmin):
    list_display = ('video_title',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(HeroImages,HeroImagesAdmin)
admin.site.register(VideoBannerFront,VideoBannerFrontAdmin)
admin.site.register(VideoBannerInside,VideoBannerInsideAdmin)

