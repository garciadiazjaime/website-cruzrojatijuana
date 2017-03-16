# -*- coding: utf-8 -*-

from django.contrib import admin

from app.data.models import Section, Data_DB, TransparenciaMenu

class SectionAdmin(admin.ModelAdmin):
	list_display = ('title_sp', 'title_en', 'slug_en', 'slug_sp', 'in_main_menu', 'in_footer')
	search_fields = ['title_en', 'title_sp', 'slug_en', 'slug_sp']
	list_filter = ['in_main_menu', 'in_footer']	

class DataAdmin(admin.ModelAdmin):
	list_display = ( 'id', 'section', 'text_en', 'text_sp')
	search_fields = ['text_en', 'text_sp']
	list_filter = ['section']	

class TransparenciaMenuAdmin(admin.ModelAdmin):
	list_display = ( 'title_sp', 'title_en', 'href_sp', 'href_en', 'alt')
	search_fields = ['href_sp', 'title_sp', 'href_en', 'title_en', 'alt']

admin.site.register(Section, SectionAdmin)
admin.site.register(Data_DB, DataAdmin)
admin.site.register(TransparenciaMenu, TransparenciaMenuAdmin)