from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#lang:0:espanish
#lang:1:engish

urlpatterns = patterns('',
    #ESPANISH
    url(r'^$', 'app.front.views.home', {'lang':0}, name='inicio'),
    url(r'^inicio$', 'app.front.views.home', {'lang':0}, name='inicio'),
    url(r'^nosotros$', 'app.front.views.about_us', {'lang':0}, name='nosotros'),
    	url(r'^nosotros/(?P<tag>[^/]+)$', 'app.front.views.about_us', {'lang':0}, name='nosotros'),
    url(r'^hospital$', 'app.front.views.hospital', {'lang':0}, name='hospital'),
    	url(r'^hospital/(?P<tag>[^/]+)$', 'app.front.views.hospital', {'lang':0}, name='hospital'),
    url(r'^ambulancias$', 'app.front.views.ambulance', {'lang':0}, name='ambulancias'),
    	url(r'^ambulancias/(?P<tag>[^/]+)$', 'app.front.views.ambulance', {'lang':0}, name='ambulancias'),
	url(r'^donativos$', 'app.front.views.donations', {'lang':0}, name='donativos'),
    	url(r'^donativos/(?P<tag>[^/]+)$', 'app.front.views.donations', {'lang':0}, name='donativos'),
	url(r'^transparencia$', 'app.front.views.transparency', {'lang':0}, name='transparencia'),
    	url(r'^transparencia/(?P<tag>[^/]+)$', 'app.front.views.transparency', {'lang':0}, name='transparencia'),
    url(r'^contacto$', 'app.front.views.contact', {'lang':0}, name='contacto'),
    	url(r'^contacto/(?P<tag>[^/]+)$', 'app.front.views.contact', {'lang':0}, name='contacto'),
    #url(r'^noticias$', 'app.front.views.news', {'lang':0}, name='noticias'),
    #	url(r'^noticias/(?P<tag>[^/]+)$', 'app.front.views.news', {'lang':0}, name='centro_capacitacion'),
    url(r'^centro-capacitacion$', 'app.front.views.training_center', {'lang':0}, name='centro_capacitacion'),
        url(r'^centro-capacitacion/(?P<tag>[^/]+)$', 'app.front.views.preparate', {'lang':0}, name='centro_capacitacion'),
    url(r'^preparate$', 'app.front.views.preparate', {'lang':0}, name='preparate'),
        url(r'^preparate/(?P<tag>[^/]+)$', 'app.front.views.preparate', {'lang':0}, name='preparate'),
        
    
    #ENGLISH
    url(r'^home$', 'app.front.views.home', {'lang':1}, name='home'),
    url(r'^about-us$', 'app.front.views.about_us', {'lang':1}, name='about-us'),
        url(r'^about-us/(?P<tag>[^/]+)$', 'app.front.views.about_us', {'lang':1}, name='about-us'),
    url(r'^the-hospital$', 'app.front.views.hospital', {'lang':1}, name='the-hospital'),
        url(r'^the-hospital/(?P<tag>[^/]+)$', 'app.front.views.hospital', {'lang':1}, name='the-hospital'),
    url(r'^ambulance$', 'app.front.views.ambulance', {'lang':1}, name='ambulance'),
        url(r'^ambulance/(?P<tag>[^/]+)$', 'app.front.views.ambulance', {'lang':1}, name='ambulance'),
    url(r'^donations$', 'app.front.views.donations', {'lang':1}, name='donations'),
        url(r'^donations/(?P<tag>[^/]+)$', 'app.front.views.donations', {'lang':1}, name='donations'),
    url(r'^transparency$', 'app.front.views.transparency', {'lang':1}, name='transparency'),
        url(r'^transparency/(?P<tag>[^/]+)$', 'app.front.views.transparency', {'lang':1}, name='transparency'),
    url(r'^contact$', 'app.front.views.contact', {'lang':1}, name='contact'),
        url(r'^contact/(?P<tag>[^/]+)$', 'app.front.views.contact', {'lang':1}, name='contact'),
		    url(r'^training-center$', 'app.front.views.training_center', {'lang':1}, name='training-center'),
    url(r'^news$', 'app.front.views.news', {'lang':1}, name='news'),
        url(r'^news/(?P<tag>[^/]+)$', 'app.front.views.news', {'lang':1}, name='news'),
    url(r'^plan-and-prepare$', 'app.front.views.preparate', {'lang':1}, name='preparate'),
         url(r'^plan-and-prepare/(?P<tag>[^/]+)$', 'app.front.views.preparate', {'lang':1}, name='preparate'),

    #EXTRAS
    url(r'^get_last_tweets$', 'app.front.views.get_last_tweets', name='get_last_tweets'),    
    url(r'^send_mail_form$', 'app.front.views.send_mail_form', name="send_mail" ),
)
