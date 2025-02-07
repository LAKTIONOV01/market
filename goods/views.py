from django.shortcuts import render
from goods.models import Product, Categories
from django.core.paginator import Paginator
from goods.utils import q_search
# Create your views here.


def catalog(request, category_slug=None):

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Product.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = Product.objects.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = Product.objects.order_by(order_by)

    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 3)

    current_page = paginator.page(int(page))

    context = {
        'products': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    context = {
        'product': Product.objects.get(slug=product_slug)
    }
    return render(request, 'goods/product.html', context)