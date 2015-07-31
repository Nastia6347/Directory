from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/img')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    slug = models.CharField(max_length=70, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)


class Product(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/img', blank=True, null=True)
    category = models.ForeignKey(Category)
    slug = models.CharField(max_length=70, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)