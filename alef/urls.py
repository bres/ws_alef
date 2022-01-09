from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings #for development
from django.conf.urls.static import static #for development
 
urlpatterns = [
    path('admin/',include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securealefatelier2005/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('store/', include('store.urls', namespace='store')),
    path('cart/', include('carts.urls', namespace='carts')),
    path('success/',views.success,name='success'),
    path('wholesale/',views.wholesale,name='wholesale'),

    #orders
    path('orders/', include('orders.urls', namespace='orders'))

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
