# -*- coding: utf-8 -*-
import re
import unidecode


class Menu(object):

	items = [
		[#ESPANISH			
			{								
				'title': 'Inicio',
				'href': 'inicio',
			},
			{				
				'title': 'Nosotros',
				'href': 'nosotros',
				'in_footer': '',
				'child':[
					{
						'title': 'Misión',
						'href': 'mision',
					},
					{
						'title': 'Siete Principios de Cruz Roja',
						'href': 'siete-principios-cruz-roja',
					},
					{
						'title': 'Institucionalidad y Transparencia',
						'href': 'institucionalidad-transparencia',
					},
					{
						'title': 'Equipo de trabajo',
						'href': 'equipo-trabajo',
					},
					{
						'title': 'Voluntariado',
						'href': 'voluntariado',
					},
					{
						'title': 'Historia',
						'href': 'historia',
					},
				]
			},
			{				
				'title': 'Hospital',
				'href': 'hospital',
				'in_footer': '',
				'child':[
					{
						'title': 'Servicios',
						'href': 'servicios',
					},
					{
						'title': 'Médicos especialistas',
						'href': 'medicos-especialistas',
					},
					{
						'title': 'Instalaciones',
						'href': 'instalaciones',
					},
					{
						'title': 'Banco de Sangre',
						'href': 'banco-sangre',
					},
				]
			},
			{				
				'title': 'Ambulancias',
				'href': 'ambulancias',
				'in_footer': '',
				'child':[
					{
						'title': 'Equipo',
						'href': 'equipo',
					},
					{
						'title': 'Bases de Ambulancia',
						'href': 'bases-ambulancia',
					},
				]
			},
			{				
				'title': 'Donar',
				'href': 'donativos',
			},
			{				
				'title': 'Transparencia',
				'href': 'transparencia',
				'in_footer': '',
				'child':[
					{
						'title': 'Servicios a la Comunidad',
						'href': 'servicios-comunidad',
					},
					{
						'title': 'Ingresos y Egresos',
						'href': 'ingresos-egresos',
					},
					{
						'title': 'Donativos',
						'href': 'donativos',
					},
					{
						'title': 'Recuperación',
						'href': 'recuperacion',
					},
					{
						'title': 'Proyectos',
						'href': 'proyectos',
					},
				]
			},
			{				
				'title': 'Contacto',
				'href': 'contacto',
				'in_footer': '',
				'child':[
					{
						'title': 'Ubicación',
						'href': 'ubicacion',
					},
					{
						'title': 'Forma de Contacto',
						'href': 'forma-contacto',
					},
					{
						'title': 'Directorio',
						'href': 'directorio',
					},
				]
			},			
			{				
				'title': 'Noticias',
				'href': 'blog',
			},			
			{				
				'title': 'Capacitación',
				'href': 'centro-capacitacion',
			},	
		],
		[#ENGLISH			
			{								
				'title': 'Home',
				'href': 'home',
			},
			{				
				'title': 'About us',
				'href': 'about-us',
				'in_footer': '',
				'child':[
					{
						'title': 'Mission',
						'href': 'mission',
					},
					{
						'title': 'Fundamental Principles',
						'href': 'fundamental-principles',
					},
					{
						'title': 'Transparency and Institutionalism',
						'href': 'transparency-institutionalism',
					},
					{
						'title': 'Work Force',
						'href': 'work-force',
					},
					{
						'title': 'Voluntary Work',
						'href': 'voluntary-work',
					},
					{
						'title': 'History',
						'href': 'history',
					},
				]
			},
			{				
				'title': 'Hospital',
				'href': 'the-hospital',
				'in_footer': '',
				'child':[
					{
						'title': 'Services',
						'href': 'services',
					},
					{
						'title': 'Especialized Consultation',
						'href': 'especialized-consultation',
					},
					{
						'title': 'Hospitalization Area Facilities',
						'href': 'hospitalization-area-facilities',
					},
					{
						'title': 'Blood Bank',
						'href': 'blood-bank',
					},
				]
			},
			{				
				'title': 'Ambulance',
				'href': 'ambulance',
				'in_footer': '',
				'child':[
					{
						'title': 'Equipment',
						'href': 'equipment',
					},
					{
						'title': 'Strategic Ambulance Stations',
						'href': 'strategic-ambulance-stations',
					},
				]
			},
			{				
				'title': 'Donations',				
				'href': 'donations',
			},
			{				
				'title': 'Transparency',
				'href': 'transparency',
				'in_footer': '',
				'child':[
					{
						'title': 'Community Service',
						'href': 'community-service',
					},
					{
						'title': 'Income and Outcome',
						'href': 'income-outcome',
					},
					{
						'title': 'Donation',
						'href': 'donation',
					},
					{
						'title': 'Recovery Rates',
						'href': 'recovery-rates',
					},
					{
						'title': 'Projects',
						'href': 'projects',
					},
				]
			},
			{				
				'title': 'Contact',
				'href': 'contact',
				'in_footer': '',
				'child':[
					{
						'title': 'Location',
						'href': 'location',
					},
					{
						'title': 'Contact Form',
						'href': 'contact-form',
					},
					{
						'title': 'Directory',
						'href': 'directory',
					},
				]
			},			
			{				
				'title': 'News',
				'href': 'blog',
			},					
			{				
				'title': 'Training',
				'href': 'training-center',
			},
		],
	]


	def get_main_menu(self, section, lang):
		response = ''		
		for row in self.items[lang]:
			is_active = 'active' if row['href'] == section else ''			
			response += "<li id=\"m_"+row['href']+"\" class=\"" + is_active + " \"><a href=\"/"+row['href']+"\" title=\""+row['title'] +"\"><span>"+row['title']+"</span></a></li>"

		response = "<ul class=\"menu\">" + response + "</ul>"
		return response

	def get_footer_menu(self, lang):
		response = ''		
		for row in self.items[lang]:
			if 'in_footer' in row:
				child = self.get_child(row['href'], row['child']) if 'child' in row else ''
				response += "<li id=\"m_"+row['href']+"\"><a href=\"/"+row['href']+"\" title=\""+row['title'] +"\"><span>"+row['title']+"</span></a> " + child + " </li>"
		response = "<ul class=\"menu\">" + response + "</ul>"
		return response

	def get_child(self, section, data):
		response = ''		
		for row in data:
			response += "<li><a href=\"/"+ section + '/' + row['href']+"\" title=\""+row['title'] +"\"><span>"+row['title']+"</span></a></li>"
		response = "<ul class=\"child\">" + response + "</ul>"
		return response

	def get_footer(self, section):
		response = ''		
		for row in self.items:
			if row['href'] not in 'testimoniales,contacto':
				child = self.get_child(row['href'], row['child']) if row.has_key('child') else ''
				if row['href'] == section:
					response += "<li class=\"active \"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a> "+ child +"</li>"
				else:
					response += "<li><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a>"+ child +"</li>"					
		if len(response):
			response = "<ul>" + response + "</ul>"
		return response