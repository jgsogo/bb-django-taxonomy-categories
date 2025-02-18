#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin

from taxonomy.admin import TaxonAdmin
from taxonomy.contrib.category_tree.models import Category

class CategoryAdmin(TaxonAdmin):
    list_display = ('title', 'breadcrumb')
    prepopulated_fields = {'slug': ('title',)}
    mptt_level_indent = 20

admin.site.register(Category, CategoryAdmin)