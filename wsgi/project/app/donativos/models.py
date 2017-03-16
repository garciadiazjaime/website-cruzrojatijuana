# -*- coding: utf-8 -*-

from django.db import models


class Campana(models.Model):
	alt = models.CharField(max_length=140)
	thumbnail = models.FileField(upload_to='app/campana/th')
	big_image = models.FileField(upload_to='app/campana')
	weight = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.alt

	class Meta:
		verbose_name = "Campaña"
		verbose_name_plural = "Campañas"

class Categoria(models.Model):
	title = models.CharField(max_length=140)
	css_class = models.CharField(max_length=140, blank=True, null=True)

	def __unicode__(self):
		return self.title

class Logros(models.Model):
	CATEGORIES_CHOICES = (
        ('Ambulancia', 'Ambulancia'),
        ('Hospital', 'Hospital'),
        ('Centro de Capacitaci&oacute;n', 'Centro de Capacitación'),
    )
	text_sp = models.CharField(max_length=140, blank=True, null=True)
	text_en = models.CharField(max_length=140, blank=True, null=True)
	weight = models.IntegerField(blank=True, null=True)
	link_sp = models.URLField(max_length=400, blank=True, null=True)
	link_en = models.URLField(max_length=400, blank=True, null=True)
	category =  models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.text_sp

	class Meta:
		verbose_name = "Logros"
		verbose_name_plural = "Logros"

class Image(models.Model):
	alt = models.CharField(max_length=140, blank=True, null=True)
	image = models.FileField(upload_to='app/images')	

	class Meta:		
		verbose_name_plural = 'Imagenes'
		verbose_name = 'Imagen'

	def __unicode__(self):
		return self.image.name


