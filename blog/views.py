from django.shortcuts import render
from shop.models import Album
from .models import Comment

def detail(request, product_id):
    producto = Album.objects.get(product_id=product_id)
    coments = Comment.objects.filter(album=producto)
    return render(request, 'core/product.html', {'producto': producto,'coments': coments})

def blog(request):
    return render(request, 'core/blog.html')

