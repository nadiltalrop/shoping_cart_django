from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from.models import Product,Category


def allProCat(request,c_slug=None):
    c_page = None
    products=None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.all().filter(category=c_page,available=True)
    else:
        products = Product.objects.all()

    paginator = Paginator(products,3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    
    context = {
        'products': products,
        'c_page': c_page
    }
    return render(request, 'category.html',context=context)


def product_details(request,cat_slug,prod_slug):
    try:
        product = Product.objects.get(category__slug=cat_slug,slug=prod_slug)
    except Exception as e:
        raise e
    
    
    context = {
        'product': product
    }

    return render(request, 'product_details.html',context=context)