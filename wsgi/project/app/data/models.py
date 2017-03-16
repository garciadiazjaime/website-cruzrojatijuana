from django.db import models

class Section(models.Model):
	title_sp = models.CharField(max_length=140)
	title_en = models.CharField(max_length=140)
	slug_sp = models.CharField(max_length=140)
	slug_en = models.CharField(max_length=140)
	in_main_menu = models.BooleanField(default=False)
	in_footer = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title_en

class Data_DB(models.Model):
	text_en = models.TextField(blank=True, null=True)
	text_sp = models.TextField(blank=True, null=True)
	section =  models.ForeignKey(Section)

	def __unicode__(self):
		return self.text_sp

class TransparenciaMenu(models.Model):
	href_sp = models.CharField(max_length=140, blank=True, null=True)
	title_sp = models.CharField(max_length=140, blank=True, null=True)
	href_en = models.CharField(max_length=140, blank=True, null=True)
	title_en = models.CharField(max_length=140, blank=True, null=True)
	alt = models.CharField(max_length=140, blank=True, null=True)

	def __unicode__(self):
		return self.title_sp