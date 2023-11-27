from django.contrib import admin
from django.conf import settings
from django.urls import path
import core.views as core_view
import shop.views as shop_view
import blog.views as blog_view


urlpatterns = [
    path('',core_view.home, name='home'),
    path('blog/',blog_view.blog, name='blog'),
    path('support/',core_view.support, name='support'),
    path('shop/', shop_view.shop, name="shop"),
    path('about/', core_view.about, name="about"),
    path('product/<str:product_id>/', blog_view.detail, name='detail'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL,
                   document_root=settings.MEDIA_ROOT)
    

    