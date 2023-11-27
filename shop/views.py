from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Album

def shop(request):
    products = Album.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj, 'page_obj': page_obj}
    return render(request, "core/shop.html",context)