from django.shortcuts import render
from directory.models import Category, Product
from directory.buisenes import list_category, list_product, bread_crumbs, list_result
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    category_list = Category.objects.filter(parent=None).order_by('title')
    category_list = list_category(category_list, 0)
    search_text = request.GET.get('q', '')
    if search_text != '':
        product_list = list_result([Product.objects.filter(title__icontains=search_text)])
    else:
        product_list = list_product(category_list)
    params = request.GET.copy()
    if 'page' in params.keys():
        del params['page']
    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'category_list': category_list, 'search_text': search_text}
    return render(request, 'index.html', args)


def category(request, slug):
    category_list = Category.objects.filter(slug=slug).order_by('title')
    bread_crumb = bread_crumbs(category_list)
    category_list = list_category(category_list, 0)
    search_text = request.GET.get('q', '')
    if search_text != '':
        product_list = list_result([Product.objects.filter(title__icontains=search_text)])
    else:
        product_list = list_product(category_list)
    params = request.GET.copy()
    if 'page' in params.keys():
        del params['page']
    category_list = list_category([bread_crumb[0].get('object')], 0)
    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    args = {'product_list': product, 'category_list': category_list, 'bread_crumbs': bread_crumb, 'search_text': search_text}
    return render(request, 'index.html', args)


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