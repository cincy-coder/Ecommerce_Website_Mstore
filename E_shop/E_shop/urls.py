from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HOME,name='home'),
    path('base/',views.BASE,name='base'),
    path('product',views.PRODUCT,name='product')
]  + static (settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
