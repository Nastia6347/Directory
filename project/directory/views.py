from django.shortcuts import render
from directory.models import Category, Product
from directory.buisenes import list_category, list_product, bread_crumbs, list_result
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def index(request):
    category_list = Category.objects.filter(parent=None).order_by('title')
    category_list = list_category(category_list, 0)
    product_list = list_product(category_list)
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'category_list': category_list}

    return render(request, 'index.html', args)


def category(request, slug):
    category_list = Category.objects.filter(slug=slug).order_by('title')
    bread_crumb = bread_crumbs(category_list)
    category_list = list_category(category_list, 0)
    product_list = list_product(category_list)
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'category_list': category_list, 'bread_crumbs': bread_crumb}
    return render(request, 'category.html', args)


def search(request):
    category_list = Category.objects.filter(parent=None).order_by('title')
    category_list = list_category(category_list, 0)
    search_text = request.GET.get('q')
    product_list = list_result([Product.objects.filter(Q(title__icontains=search_text))])
    params = request.GET.copy()
    if 'page' in params.keys():
        del params['page']
    paginator = Paginator(product_list, 3)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'category_list': category_list, 'search_text': search_text, 'params': params}
    return render(request, 'search.html', args)