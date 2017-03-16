# -*- coding: utf-8 -*-

from django.contrib import admin

from app.donativos.models import Campana, Categoria, Logros, Image
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group

#from django.contrib.sites.models import Users

class CampanaAdmin(admin.ModelAdmin):
	list_display = ( 'alt', 'thumbnail','big_image', 'weight')

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'css_class')

class LogrosAdmin(admin.ModelAdmin):
	list_display = ( 'text_sp', 'text_en', 'weight','link_sp', 'link_en', 'category')

class ImageAdmin(admin.ModelAdmin):
	list_display = ( 'image', 'alt')

admin.site.register(Campana, CampanaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Logros, LogrosAdmin)
admin.site.register(Image, ImageAdmin)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)