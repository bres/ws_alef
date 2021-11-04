from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings #for development
from django.conf.urls.static import static #for development

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('', include('accounts.urls',namespace='accounts')),
    path('store/', include('store.urls', namespace='store')),
    path('cart/', include('carts.urls', namespace='carts')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
