__author__ = 'user'
from directory.models import Product, Category


def list_category(ul, n):
        g = []
        for x in ul:
                g += [{'object': x, 'level': n, 'slug': "/".join(slug_list([x]))}]
                g += list_category(Category.objects.filter(parent=x).order_by('title'), n+1)
        return g


def list_product(category):
        ul = []
        ul += lists(category)
        n = len(ul) % 12
        if len(ul) == 0 or n > 0:
            for x in range(12-n):
                ul.append('')
        g = [ul[i:i + 4] for i in range(0, len(ul), 4)]
        return g


def lists(ul):
        g = []
        for x in ul:
                g += Product.objects.filter(category=x.get('object')).order_by('title')
        return g


def bread_crumbs(ul):
        g = []
        for x in ul:
                g += bread_crumbs(Category.objects.filter(id=x.parent_id))
                g += [{'object': x, 'slug': "/".join(slug_list([x]))}]
        return g


def slug_list(ul):
        g = []
        for x in ul:
                g += slug_list(Category.objects.filter(id=x.parent_id))
                g += [x.slug.encode()]
        return g


def list_result(ul):
        g = []
        for x in ul:
            g += x
        n = len(g) % 12
        if len(g) == 0 or n > 0:
            for x in range(12-n):
                g.append('')
        c = [g[i:i + 4] for i in range(0, len(g), 4)]
        return c