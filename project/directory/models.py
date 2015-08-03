from django.db import models
from django.db import IntegrityError, transaction
import re
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/img')
    parent = models.ForeignKey('self', blank=True, null=True)
    slug = models.CharField(max_length=70, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title
        slug_list = Category.objects.filter(slug=self.slug)
        if slug_list:
            self.slug += self.id
        super(Category, self).save(*args, **kwargs)
        # if not self.slug:
        #     self.slug = self.title
        # while True:
        #     try:
        #         with transaction.atomic():
        #             super(Category, self).save(*args, **kwargs)
        #     except IntegrityError:
        #         match_obj = re.match(r'^(.*)-(\d+)$', self.slug)
        #         if match_obj:
        #             next_int = int(match_obj.group(2)) + 1
        #             self.slug = match_obj.group(1) + '-' + str(next_int)
        #         else:
        #             self.slug += '-2'
        #     else:
        #         break

    def __unicode__(self):
        return unicode(self.title)


class Product(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/img', blank=True, null=True)
    category = models.ForeignKey(Category)
    slug = models.CharField(max_length=70, editable=False, unique=True)

    def __unicode__(self):
        return unicode(self.title)