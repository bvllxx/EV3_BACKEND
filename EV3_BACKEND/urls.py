from django.contrib import admin
from django.urls import path
import core.views as core_view
import shop.views as shop_view
from django.conf import settings

urlpatterns = [
    path('',core_view.home, name='home'),
    path('about/',core_view.about, name='about'),
    path('shop/', shop_view.shop, name="shop"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL,
                   document_root=settings.MEDIA_ROOT)
    

    