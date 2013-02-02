#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from taxonomy.models.taxon import BaseTaxon
from taxonomy.managers import TaxonManager

class CategoryManager(TaxonManager):
    def choices(self, user=None):
        qs = self.get_query_set().all()

        if user is not None and user.is_superuser:
            # superusers get to see all categories
            return qs
        else:
            # only show public categories to regular users
            return qs.filter(public=self.model.PUBLIC)

    def orphan(self, user=None):
        """ Retrieves all categories with no parent """
        return self.choices(user).filter(parent=None)


class Category(BaseTaxon):
    PUBLIC = 0
    PRIVATE = 1
    PUBLICY_CHOICES = ( (PUBLIC, _('public')), (PRIVATE, _('private')),)


    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True, help_text=_(u'Optional'))
    public = models.IntegerField(choices = PUBLICY_CHOICES)

    objects = CategoryManager()

    class MPTTMeta:
        order_insertion_by = ['slug']

    class Meta(BaseTaxon.Meta):
        db_table = 'category_tree'
        app_label = 'category_tree'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        abstract = False

    def get_name(self):
        return self.title

    def save(self, *args, **kwargs):
        if not len(self.slug.strip()):
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
