from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
import trans
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/img')
    parent = models.ForeignKey('self', blank=True, null=True)
    slug = models.CharField(max_length=70, editable=False, unique=True)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title.encode('trans'))
            slug_list = Category.objects.filter(slug=self.slug)
            if slug_list:
                self.slug += str(self.id)
            super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.title)


class Product(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/img', blank=True, null=True)
    category = models.ForeignKey(Category)
    slug = models.CharField(max_length=70, editable=False, unique=True, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)
