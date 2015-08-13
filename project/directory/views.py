from django.shortcuts import render
from directory.models import Category, Product
from directory.buisenes import list_category, list_product, bread_crumbs, list_result
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    category_list = Category.objects.filter(parent=None).order_by('title')
    category_list = list_category(category_list, 0)
    product_list = list_product(category_list)
    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'category_list': category_list}
    return render(request, 'index.html', args)


def category(request, slug):
    category_list = Category.objects.filter(slug=slug).order_by('title')
    bread_crumb = bread_crumbs(category_list)
    category_list = list_category(category_list, 0)
    product_list = list_product(category_list)
    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'bread_crumbs': bread_crumb}
    return render(request, 'search.html', args)


def search(request):
    search_text = request.GET.get('q')
    product_list = list_result([Product.objects.filter(title__icontains=search_text)])
    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'search_text': search_text}
    return render(request, 'search.html', args)