# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
	def __str__(self): 
		return self.title
		

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)


