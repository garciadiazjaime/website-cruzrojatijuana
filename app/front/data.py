# -*- coding: utf-8 -*-

class Data(object):
	
	def gral(self, lang):
		data = [
			{#SPANISH
				'page_title': 'Cruz Roja Mexicana',
				'page_subtitle': 'Cruz Roja Mexicana - Delegación Tijuana',
				'keywords': 'Cruz Roja',
				'description': 'Bienvenido al sitio oficial de la Cruz Roja Mexicana',
				'logo_title': 'Regresar a inicio',
				'logo_href': 'inicio',
				'training_title': 'Centro de Capacitación',				
				'training_href': 'centro-capacitacion',
				'get_ready_title': 'Prepárate',
				'get_ready_href': 'preparate',
				'news_title': 'Noticias',
				'news_href': 'blog',
				'credit_title': 'Créditos',
				'credit_href': 'creditos',

				'training_href': 'centro-capacitacion',
				'training_title': 'Centro de Capacitación',
				'facebook_title': 'Síguenos en Facebook',
				'facebook_href': 'https://www.facebook.com/cruzrojadetijuana',
				'twitter_title': 'Seguir a @CruzRojaTijuana',
				'twitter_href': 'https://twitter.com/CruzRojaTijuana',
				'youtube_title': 'Síguenos en Youtube',
				'youtube_href': 'http://www.youtube.com/user/comunicacionCRT',

				'donations_title': 'Donativos',
				'donations_text': 'Con tu donativo haces la diferencia',
				'donations_help_title': 'Quiero donar',
				'donations_help_href': 'donativos',
				'donations_paypal_short_title': 'Donar por medio de paypal',
				'donations_paypal_title': 'Donar por medio de paypal',
				'donations_paypal_href': 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5NL5HVNJCGK24',
				'donations_paypal_aux': 'Donar por medio de paypal',

				'copyright': 'Todos los derechos reservados © Cruz Roja 2013',

				'preparate': 
				{
					'title': 'Prepárate',
					'href': '/preparate',
					'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
					'pregunta': '¿Qué hacer en caso de...?',
					'tema': 'Incendio',
					'tema_href': '/preparate/incendio',
					'tema_respuesta_intro': '¿Estás preparado para un incendio?',
					'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
					'tema_respuesta_cierre': 'Protege tu hogar contra incendios.',
					'mas': 'Ayúdanos a prevenir accidentes',
					'mas_href': '/preparate',
				},
				'preparate_home': 
				{
					'title': 'Incendio',
					'href': 'incendio',
				},
				'preparate_nosotros': 
				{
					'title': 'Inundaciones',
					'href': 'inundaciones',
				},
				'donativos':
					{
						'title': 'Donativos',
						'href': 'donativos',
						'tipo': 
							[
								{
									'title': 'Donar en especie',
									'href': '/donativos/especie',
								},
								{
									'title': 'Donar tu tiempo',
									'href': '/donativos/tiempo',
								},
								{
									'title': 'Donar económicamente',
									'href': '/donativos/dinero',
								},
							],
					},
				'video':
				{
					'title': 'Videos',
					'subtitle': 'Cortometraje Cruz Roja Baja California',
					'mas': 'Visita nuestro canal de youtube',
					'mas_href': 'http://www.youtube.com/user/comunicacionCRT',
				},
				'credits':
				{
					'title': 'Créditos',
					'subtitle': 'Créditos y agradecimiento por su apoyo en:',
					'photo': 'Fotografía:',
					'write_to_alt': 'Escribir a',
					'translate': 'Traducción',
					'history': 'Recopilación fotografías históricas:',
					'history_credit': 'Veterano Ricardo Naranjo',
					'makeup': 'Maquillaje',
					'makeup_write': 'Escribir a',
				}, 
			},
			{#ENGLISH
				'page_title': 'Cruz Roja Mexicana',
				'page_subtitle': 'Cruz Roja Mexicana - Tijuana Delegation',
				'keywords': 'Cruz Roja',
				'description': 'Welcome to the official site of Cruz Roja Mexicana',
				'logo_title': 'Return to home',
				'logo_href': 'home',
				'training_title': 'Training Center',				
				'training_href': 'training-center',
				'get_ready_title': 'Plan and prepare',
				'get_ready_href': 'plan-and-prepare',
				'news_title': 'News',
				'news_href': 'blog',
				'credit_title': 'Credits',
				'credit_href': 'credits',

				'training_href': 'training-center',
				'training_title': 'Training Center',
				'facebook_title': 'Follow us on Facebook',
				'facebook_href': 'https://www.facebook.com/cruzrojamexicanadelegaciontijuana',
				'twitter_title': 'Follow @CruzRojaTijuana',
				'twitter_href': 'https://twitter.com/CruzRojaTijuana',
				'youtube_title': 'Follow us on Youtube',
				'youtube_href': 'http://www.youtube.com/user/comunicacionCRT',

				'donations_title': 'Donations',
				'donations_text': 'With your donations you make a difference',
				'donations_help_title': 'I want to donate',
				'donations_help_href': 'donations',
				'donations_paypal_short_title': 'Donate trough paypal',
				'donations_paypal_title': 'Donate trough paypal',
				'donations_paypal_href': 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5NL5HVNJCGK24',
				'donations_paypal_aux': 'Donate trough paypal',

				'copyright': 'All rights reserved © Cruz Roja 2013',

				'preparate': 
				{
					'title': 'Plan and prepare',
					'href': '/get_ready',
					'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
					'pregunta': 'What to do in case of…?',
					'tema': 'Fire',
					'tema_href': '/get_ready/incendio',
					'tema_respuesta_intro': 'Are you prepared for a fire?',
					'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
					'tema_respuesta_cierre': 'Protege tu hogar contra incendios.',
					'mas': 'Help us prevent accidents',
					'mas_href': '/get_ready',
				},
				'donativos':
					{
						'title': 'Donations',
						'href': 'donations',
						'tipo': 
							[
								{
									'title': 'Donate in kind',
									'href': '/donations/kind',
								},
								{
									'title': 'Donate with time',
									'href': '/donations/time',
								},
								{
									'title': 'Donate money',
									'href': '/donations/money',
								},
							],
					},
				'video':
				{
					'title': 'Videos',
					'subtitle': 'Cortometraje Cruz Roja Baja California',
					'mas': 'Visit our youtube channel',
					'mas_href': 'http://www.youtube.com/user/comunicacionCRT',
				},
				'credits':
				{
					'title': 'Credits',
					'subtitle': 'Credit and thanks for their support in:',
					'photo': 'Photography:',
					'write_to_alt': 'Write to',
					'translate': 'Translation',
					'history': 'Compilation of historical photographies:',
					'history_credit': 'Ricardo Naranjo',
					'makeup': 'Make up',
					'makeup_write': 'Write to',
				}, 
			},
		]
		return data[lang]

	def home(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'inicio',
							'section_lang': 'home',
							'sp_active': 'current',
							'page_subtitle': 'Cruz Roja Mexicana - Delegación Tijuana',
							'has_cycle': 'true',
							'has_fancybox': 'true',
							'has_timeline': 'true',
						},
					'header': 
						{
							'title': 'Seamos todos hermanos',
							'conocenos_title': 'conócenos',
							'conocenos_href': 'nosotros',
							'donar_title': 'quiero donar',
							'donar_href': 'donativos',
							'donar_porfavor_title': 'Por favor, dona',
							'donar_especie_title': 'Donar en especie',
							'donar_especie_href': '/donativos/especie',
							'donar_tiempo_title': 'Donar tu tiempo',
							'donar_tiempo_href': '/donativos/tiempo',
							'donar_dinero_title': 'Donar dinero',
							'donar_dinero_href': '/donativos/dinero',
							'gallery': 
							[
								{
									'src': '',
									'title': '',
								},
								{
									'src': '',
									'title': '',
								},
							],
							'news_href': 'blog',
							'news_title': 'Noticias',
							'news_read': 'Leer noticia',
							'news_read_more': 'Leer más noticias',	
							'scroll_down': 'bajar',
						},
					'our_mission':
						{
							'title':'Nuestra misión',
							'slider':'<div class="slider_frame"><p>Auxiliar a todo<br /> ser humano<br /> en riesgo</p></div><div class="slider_frame"><p>Atención eficiente<br /> de emergencias y<br /> desastres</p></div><div class="slider_frame"><p>Promover la<br /> capacitación<br /> del tijuanense</p></div>',
						},	
					'hospital':
						{
							'description': 'Nuestra misión es auxiliar sin distinción de raza, condición económica o credo político a todo ser humano cuya vida y salud se encuentre en riesgo, ofreciendo atención eficiente en casos de emergencia y situaciones de desastre, así como promover la capacitación del tijuanense.',
							'link_href': 'nosotros',
							'link_title': 'Conócenos',
						},
					'ambulancia':
						{
							'titles': 'Servicio de ambulancia, rescate y hospital<br /> las <em>24 hrs</em> del día, los <em>365 días</em> del año.',
							'tel': 'Llama al 066 para atención médica urgente',
							'socorro_title': 'Socorrismo, ambulancias <br> y rescate',
							'socorro_href': '/ambulancias/equipo',
							'socorro_desc': '<p>Atendemos gratuitamente el 98% del servicio de ambulancia y rescate a través del llamado de emergencia al 066.</p>',
							'socorro_link_href': 'ambulancias',
							'socorro_link_title': 'Conoce más de socorrismo y ambulancias',
							'socorro_link_aux': 'Conoce más',
							'hospital_href': '/ambulancias/equipo',
							'hospital_title': 'Hospital de<br> Trauma',
							'hospital_desc': '<p>Ofrecemos servicios médicos de calidad con una cuota de recuperación para continuar atendiendo a la comunidad más vulnerable, logrando brindar el 60% del servicio de  trauma que se necesita en Tijuana.</p><p>Contamos con Banco de Sangre, vital para salvar vidas. </p>',
							'hospital_link_title': 'Conoce más sobre el hospital de servicios médicos',
							'hospital_link_aux': 'Conoce más',
							'hospital_link_href': '/hospital',
							'capacitacion_title': 'Centro de Capacitación',
							'capacitacion_href': 'centro-capacitacion',
							'capacitacion_desc': 'Promovemos la educación por una comunidad preparada para salvar vidas en cualquier emergencia o desastre:',
							'capacitacion_list': '<li><span>Profesionales de Enfermería y Paramédicos.</span></li> <li><span>Curso de primeros auxilios certificado.</span></li> <li><span>Pláticas de prevención de accidentes y primeros auxilios. </span></li> <li><span>Cursos de primeros auxilios, prevención y sobrevivencia.</span></li><li><span>Curso de ACLS y BLS avalados por la Asociación Americana del Corazón.</span></li>',
							'capacitacion_mas_title': 'CAPACÍTATE',
							'capacitacion_mas_href': 'centro-capacitacion',
						},
					'logros':
						{
							'img_datos': 'index_img_donaciones.png',
							'img_alt': 'Nos sostenemos gracias a 70% Donativos y un 30% de Cuotas de recuperación',
							'desc': 'Somos una Institución de Asistencia Privada (I.A.P) con carácter voluntario y no lucrativo; nos sostenemos 70% de donativos y 30% de cuotas de recuperación del servicio hospitalario.',
							'transparencia_title': 'Transparencia',
							'transparencia_href': 'transparencia',
							'logros_title': 'Logros 2013 <em class="red_text">¡Gracias a tí!</em>',
						},
					'donar':
						{
							'title': 'Dona Ahora',
							'href': 'donativos',
							'especie':
								{
									'title': 'Especie',
									'href': '/donativos/especie',
									'items': 
									[
										{'title': 'Donación de Sangre'},
										{'title': 'Tu chatarra de metal'},
										{'title': 'Equipo médico y medicamento'},
										{'title': 'Espacios publicitarios'},
										{'title': 'Alimentos'},
										{'title': 'Asesoría profesional'},
										{'title': 'Entre otros'},
									]
								},
							'tiempo':
								{
									'title': 'Tiempo',
									'href': '/donativos/tiempo',
									'items': 
									[
										{'title': 'Súmate a nuestro equipo de voluntarios'},
										{'title': 'Programas de servicio social y prácticas profesionales'},
									]
								},
							'dinero':
								{
									'title': 'Dinero',
									'href': '/donativos/programa-benefactor-distinguido',
									'desc': 'Realiza tu donativo por medio del sistema Paypal, depósito a cuentas bancarias y por International Community Foundation.',
								},
							'link_donativos_title': 'Donativos',
							'link_donativos_href': '/donativos/especie',
							'link_contactanos_title': 'Contáctanos',
							'link_contactanos_href': '/contacto',
							'link_conocenos_title': 'Donativos',
							'link_conocenos_href': '/donativos/programa-benefactor-distinguido',
						},
						'preparate': 
						{
							'title': 'Prepárate',
							'href': '/preparate',
							'class': 'incendio',
							'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
							'pregunta': '¿Qué hacer en caso de...?',
							'tema': 'Incendio',
							'tema_href': '/preparate/incendio',
							'tema_respuesta_intro': '¿Estás preparado para un incendio?',
							'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
							'tema_respuesta_cierre': 'Protege tu hogar contra incendios.',
							'mas': 'Ayúdanos a prevenir accidentes',
							'mas_href': '/preparate',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'inicio',
							'section_lang': 'home',
							'sp_active': 'current',
							'page_subtitle': 'Cruz Roja Mexicana - Delegación Tijuana',
							'has_cycle': 'true',
							'has_fancybox': 'true',
							'has_timeline': 'true',
						},
					'header': 
						{
							'title': 'Let’s all be brothers	and sisters',
							'conocenos_title': 'Get to know us',
							'conocenos_href': 'about-us',
							'donar_title': 'I want to donate',
							'donar_href': 'donations',
							'donar_porfavor_title': 'Please, donate',
							'donar_especie_title': 'Donate in kind',
							'donar_especie_href': '/donations/kind',
							'donar_tiempo_title': 'Donate with time',
							'donar_tiempo_href': '/donations/time',
							'donar_dinero_title': 'Donate money',
							'donar_dinero_href': '/donations/money',
							'gallery': 
							[
								{
									'src': '',
									'title': '',
								},
								{
									'src': '',
									'title': '',
								},
							],
							'news_href': 'blog',
							'news_title': 'News',
							'news_read': 'Read news',
							'news_read_more': 'Read more',	
							'scroll_down': 'Scroll down',
						},
					'our_mission':
						{
							'title':'Our mission',
							'slider':'<div class="slider_frame small"><p>Is to assist every<br /> human being<br /> whose life is at risk</p></div><div class="slider_frame small"><p>Efficient attention<br /> in emergency cases and<br /> disaster situations</p></div><div class="slider_frame small"><p>Promote training throughout the community of Tijuana</p></div>',
						},
					'hospital':
						{
							'description': 'Our mission is to assist every human being regardless of race, economical condition or political creed, whose life is at risk by offering efficient attention in emergency cases and disaster situations; as well as to promote training throughout the community of Tijuana.',
							'link_href': 'about-us',
							'link_title': 'About Us',
						},
					'ambulancia':
						{
							'titles': 'Ambulance, rescue and hospital <br />services <em>24/7-365</em>',
							'tel': 'Call to 066 for urgent medical attention',
							'socorro_title': 'Emergency <br />Services',
							'socorro_href': '/ambulance/team',
							'socorro_desc': '<p>Our assistance in rescue and ambulance needs is 98% free of charge. Contact us through the emergency phone number 066.</p>',
							'socorro_link_href': 'ambulance',
							'socorro_link_title': 'Know more about emergency services and ambulances',
							'socorro_link_aux': 'Know more',
							'hospital_href': '/ambulance/team',
							'hospital_title': 'Trauma <br />Hospital ',
							'hospital_desc': '<p>We offer quality medical services charging a recovery rate to be able to keep assisting the most vulnerable community, succeeding in covering 60% of the Traumatology (Trauma) needs of Tijuana.</p><p>Our hospital has its own Blood Bank, which is vital for saving lives.</p>',
							'hospital_link_title': 'Know more about the medical services hospital',
							'hospital_link_aux': 'Know more',
							'hospital_link_href': '/hospital',
							'capacitacion_title': 'Training Center',
							'capacitacion_href': 'training-center',
							'capacitacion_desc': 'We promote education to build a community prepared to save lives in any type of emergency or disaster:',
							'capacitacion_list': '<li><span>Infirmary professionals and Paramedics.</span></li> <li><span>Certified first aid course.</span></li> <li><span>First aid and accident prevention talks. </span></li> <li><span>Accident prevention, first aid, and survival courses.</span></li> <li><span>Course of ACLS and BLS endorsed by the American Heart Association.</span></li>',
							'capacitacion_mas_title': 'Take a class',
							'capacitacion_mas_href': 'training-center',
						},
					'logros':
						{
							'img_datos': 'index_img_donaciones_eng.png',
							'img_alt': 'Our resources are 70% in donations, and 30% in recovery rates of the hospital services.',
							'desc': 'We are a Non-profit Institution of a voluntary and non-lucrative nature. Our resources are 70% in donations, and 30% in recovery rates of the hospital services. ',
							'transparencia_title': 'transparency',
							'transparencia_href': 'transparency',
							'logros_title': '2013 Achievements <em class="red_text">Thanks to you</em>',
						},
					'donar':
						{
							'title': 'Donations',
							'href': 'donations',
							'especie':
								{
									'title': 'In Kind',
									'href': '/donations/kind',
									'items': 
									[
										{'title': 'Blood Donation'},
										{'title': 'Metal Scrap'},
										{'title': 'Medical Equipment and Medicine'},
										{'title': 'Advertising Spaces'},
										{'title': 'Food'},
										{'title': 'Professional Advice'},
										{'title': '…and more'},
									]
								},
							'tiempo':
								{
									'title': 'Time',
									'href': '/donations/time',
									'items': 
									[
										{'title': 'Be part of our volunteer team'},
										{'title': 'Social Service and Professional Practice'},
									]
								},
							'dinero':
								{
									'title': 'Money',
									'href': '/donations/distinguished-benefactor-program',
									'desc': 'You can donate through PayPal, or make deposits to bank accounts and through the International Community Foundation.',
								},
							'link_donativos_title': 'Donations',
							'link_donativos_href': '/donations/kind',
							'link_contactanos_title': 'Contact us',
							'link_contactanos_href': '/contact',
							'link_conocenos_title': 'Donations',
							'link_conocenos_href': '/donations/distinguished-benefactor-program',
						},
						'preparate': 
							{
								'title': 'Plan and prepare',
								'href': '/plan-and-prepare',
								'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
								'pregunta': 'What to do in case of…?',
								'tema': 'Fire',
								'tema_href': '/plan-and-prepare/fires',
								'tema_respuesta_intro': 'Are you prepared for a fire?',
								'tema_respuesta_desc': 'This is what you can do to prepare yourself in the event of such emergency.',
								'tema_respuesta_cierre': 'Protect your home from fires',
								'mas': 'Help us prevent accidents',
								'mas_href': '/plan-and-prepare',
							},
				},
			]		
		return data[lang]

	def about_us(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'nosotros',
							'section_lang': 'about-us',
							'page_subtitle': 'Nosotros',
							'has_cycle': 'true',
							'has_fancybox': 'true',
							'has_timeline': 'true',
						},
					'mision':
						{
							'title': 'Misión',
							'desc': 'Auxiliar sin distinción de raza, condición económica o credo político a todo ser humano cuya vida y salud se encuentre en riesgo, ofreciendo atención eficiente en casos de emergencia y situaciones de desastre, así como promover la capacitación del tijuanense.',
							'slogan': '<span class="hidden"">"</span>Seamos<br> todos <br>hermanos"',
						},
					'principios':
						{
							'title': 'Siete Principios',
							'desc': 'Proclamados en Viena en 1965, los siete Principios Fundamentales crean un vínculo de unión entre las Sociedades Nacionales de la Cruz Roja y de la Media Luna Roja, el Comité Internacional y la Federación Internacional de Sociedades. Estos Principios garantizan la continuidad del Movimiento y su labor humanitaria. Todo lo que la Institución es y hace está inscrito en ellos.',
							'list':
								[
									{
										'title': 'Humanidad',
										'id': 'prin_humanidad',
									},
									{
										'title': 'Imparcialidad',
										'id': 'prin_imparcialidad',
									},
									{
										'title': 'Neutralidad',
										'id': 'prin_neutralidad',
									},
									{
										'title': 'Independencia',
										'id': 'prin_independendiente',
									},
									{
										'title': 'Voluntariado',
										'id': 'prin_voluntariado',
									},
									{
										'title': 'Unidad',
										'id': 'prin_unidad',
									},
									{
										'title': 'Universalidad',
										'id': 'prin_universalidad',
									},
								]
						},
					'institucion': 
						{
							'title': 'Institucionalidad y <br>Transparencia',
							'desc': 'El Centro Mexicano para la Filantropía nos avala por contar con el nivel óptimo de Institucionalidad y Transparencia en cumplimiento con las disposiciones legales y fiscales establecidas, transparencia en el manejo de los recursos, estructura organizacional eficiente, equilibrada y sostenible que permite desarrollar profesionalmente nuestro trabajo y generar confianza en los diversos públicos.',
							'link_href': 'transparencia',
							'link_title': 'Transparencia',
							'img': 'img_transparencia',
						},
					'equipo': 
						{
							'title': 'Equipo de trabajo',
							'desc': '<strong>215</strong> personas trabajando todos los días, sumando esfuerzos con más de <strong>500</strong> voluntarios, ciudadanía, empresas, instituciones, dependencias y organizaciones de la sociedad civil. ',
							'subtitle': '¡Cruz Roja somos todos!',
							'third_title':'Consejo Directivo',
							'list_a': 
								{
									'title':'Coordinaciones:',
									'items': ['Socorrismo', 'Capacitación', 'Servicios médicos', 'Enfermería', 'Damas voluntarias', 'Veteranos', 'Juventud', 'Voluntariado', 'Procuración de fondos', 'Comunicación e imagen'],
								},
							'list_b': 
								{
									'title': 'Administrativa:',
									'items': ['Dirección general', 'Recursos humanos', 'Contabilidad', 'Compras', 'Sistemas', 'Trabajo social', 'Almacén', 'Planeación'],
								}							
						},
					'voluntarios':
						{
							'title': 'Voluntariado',
							'desc': 'La creación del movimiento Internacional de Cruz Roja tiene el objetivo de encausar a niños, jóvenes y adultos hacia el trabajo comunitario conforme a la filosofía Institucional de los Siete Principios para impulsar el cumplimiento de nuestra misión.',
							'beneficios':
								{
									'title': 'Beneficios',
									'list': ['Capacitación.', 'Formación y crecimiento humano.', 'Servicio social.', 'Prácticas profesionales.'],
								},
							'slogan': '¡Súmate al movimiento más grande el mundo!',
							'slogan_b': 'El voluntariado lo hacemos todos”',
							'link':
								{
									'href': '/contacto',
									'title': 'Súmate',
								},
							'contacto':
								{
									'title': 'Recursos Humanos.',
									'tel': '(664) 608.67.09',
									'mail': 'recursoshumanos@cruzrojatijuana.org.mx',
									'alt': 'Escríbenos a recursos humanos',
								}
						},
						
					'historia':
						{
							'title': 'Historia',
							'subtitle': 'Cruz Roja Mexicana Delegación Tijuana.'
						},
						'preparate': 
						{
							'title': 'Prepárate',
							'href': '/preparate/inundaciones',
							'class': 'inundacion',
							'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
							'pregunta': '¿Qué hacer en caso de...?',
							'tema': 'Inundaciones',
							'tema_href': '/preparate/inundaciones',
							'tema_respuesta_intro': '¿Estás preparado para una inundación?',
							'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
							'tema_respuesta_cierre': 'Protege tu hogar contra inundaciones.',
							'mas': 'Ayúdanos a prevenir accidentes',
							'mas_href': '/preparate',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 								
							'section': 'nosotros',
							'section_lang': 'about-us',
							'page_subtitle': 'About us',
							'has_cycle': 'true',
							'has_fancybox': 'true',
							'has_timeline': 'true',
						},
					'mision':
						{
							'title': 'Mission',
							'desc': 'Our mission is to assist every human being regardless of race, economical condition or political creed, whose life is at risk by offering efficient attention in emergency cases and disaster situations; as well as to promote training throughout the community of Tijuana.',
							'slogan': '<span class="hidden"">"</span>Let’s all be<br> brothers<br> and sisters"',
						},
					'principios':
						{
							'title': 'Seven Fundamental Principles',
							'desc': 'The seven Fundamental Principles were proclaimed in Vienna in 1965 and create a bond between the National Societies of the Red Cross and the Red Crescent, the International Committee and the International Federation of Societies. These Principles guarantee the continuity of the Movement and its humanitarian work. Every aspect of the Institution lies within these Principles: ',
							'list':
								[
									{
										'title': 'Humanity',
										'id': 'prin_humanidad',
									},
									{
										'title': 'Imparciality',
										'id': 'prin_imparcialidad',
									},
									{
										'title': 'Neutrality',
										'id': 'prin_neutralidad',
									},
									{
										'title': 'Independence',
										'id': 'prin_independendiente',
									},
									{
										'title': 'Voluntary Service',
										'id': 'prin_voluntariado',
									},
									{
										'title': 'Unity',
										'id': 'prin_unidad',
									},
									{
										'title': 'Universality',
										'id': 'prin_universalidad',
									},
								]
						},
					'institucion': 
						{
							'title': 'Transparency and<br> Institutionalism',
							'desc': 'The Mexican Center of Philanthropy (CEMEFI, by its acronym in Spanish) supports us with its high standards in Institutionalism and Transparency complying with fiscal and legal requirements, transparent resource management, efficient, balanced, and sustainable organizational structure, that allows us to do our job professionally and creates confidence in people. ',
							'link_href': 'transparency',
							'link_title': 'Transparency',
							'img': 'img_transparencia',
						},
					'equipo': 
						{
							'title': 'Work Force ',
							'desc': '<strong>215</strong> people are working daily along with over <strong>500</strong> volunteers, citizens, companies, institutions, and social organizations…  ',
							'subtitle': 'We Are All the Red Cross!',
							'third_title':'Executive Board',
							'list_a': 
								{
									'title':'Coordinations:',
									'items': ['Emergency Services', 'Training', 'Medical Services', 'Infirmary', 'Volunteer Ladies', 'Veterans', 'Youth', 'Volunteers', 'Fund Raising', 'Image and Communication'],
								},
							'list_b': 
								{
									'title': 'Administrative:',
									'items': ['General Management', 'Human Resources', 'Accounting', 'Purchasing Department', 'Information Systems', 'Social Services', 'Warehouse', 'Planning'],
								}					
						},
					'voluntarios':
						{
							'title': 'Voluntary Work',
							'desc': 'The creation of the Red Cross movement has the objective of promoting volunteer work among children, teenagers, and adults, in accordance to the Institutional philosophy of the Fundamental Principles to motivate the fulfillment of our mission.  ',
							'beneficios':
								{
									'title': 'Benefits',
									'list': ['Training.', 'Education and Human Development.', 'Social Service.', 'Professional Practice.'],
								},
							'slogan': 'Join the Largest Movement in the World!',
							'slogan_b': 'We all create volunteering”',
							'link':
								{
									'href': '/contact',
									'title': 'Join Us',
								},
							'contacto':
								{
										'title': 'Human Resources.',
										'tel': '(664) 608.67.09',
										'mail': 'recursoshumanos@cruzrojatijuana.org.mx',
										'alt': 'Write to human resources',
								}
						},

					'historia':
						{
							'title': 'History',
							'subtitle': 'Cruz Roja Mexicana Tijuana.'
						},
					'preparate':
						{
							'title': 'Plan and prepare',
							'href': '/plan-and-prepare',
							'class':'inundacion',
							'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
							'pregunta': 'What to do in case of…?',
							'tema': 'Floods',
							'tema_href': '/plan-and-prepare/floods',
							'tema_respuesta_intro': 'Are you prepared for a fire?',
							'tema_respuesta_desc': 'This is what you can do to prepare yourself in the event of such emergency.',
							'tema_respuesta_cierre': 'Protect your home from floods.',
							'mas': 'Help us prevent accidents',
							'mas_href': '/plan-and-prepare',
						},
				},
			]		
		return data[lang]

	def hospital(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'hospital',
							'section_lang': 'the-hospital',
							'has_cycle': 'true',
							'title': 'Hospital',
							'desc': 'En Tijuana por ser una ciudad de gran demanda de servicios de salud, establecimos  el <strong>Hospital de Trauma</strong> donde brindamos atención médica de calidad apoyados por cuotas de recuperación para continuar <strong>ayudando a la población más vulnerable</strong>.',
						},
					'lista_a': 
						[
							'Atendemos el <strong>60%</strong> del trauma que ocurre en <strong>Tijuana</strong>.',
							'Conformado por <br><strong>35 médicos y</strong> <br><strong>45 enfermeros.</strong>',
							'Más de <strong>35,000 personas</strong> atendidas al año.',
						],
					'servicios': 
						{
						'title': 'Servicios',
						'list_a':
							[
								'Urgencias',
								'Hospitalización',
								'Cirugía',
								'Sala de reanimación',
								'Cuidados intensivos adultos y pediátricos',
								'Banco de sangre',
								'Certificado médico de buena salud',
								'Radiografías y tomografías por Grupo Imagen Radiológica',
								'Análisis Clínicos por Laboratorio Certus',
							],
						'subtitle': 'Consulta externa de <br>médicos especialistas:',
						'list_b':
							[
								'Traumatología y ortopedia',
								'Otorrinolaringología',
								'Cardiología',
								'Psicología',
								'Neurología',
							],
						},
					'instalaciones':
						{
						'title': 'Instalaciones del área<br> hospitalaria:',
						'lista':
							[
								{
									'title': 'Sala de Urgencias',
									'desc': '8 camas',
								},
								{
									'title': 'Sala de Reanimación',
									'desc': '2 camas',
								},
								{
									'title': 'Quirófanos',
									'desc': '3 camas',
								},
								{
									'title': 'Área de Hospitalización',
									'desc': 'Mujeres - 4 camas<br>Hombres - 13 camas<br>Pediatría - 4 camas',
								},
								{
									'title': 'Cuidados Intensivos',
									'desc': 'Adultos - 4 camas <br>Pediatría - 2 camas',
								},
								{
									'title': 'Semi-cuidados Intensivos',
									'desc': 'Pediatría - 3 camas',
								},
								{
									'title': 'Cuna térmica',
									'desc': '1 cuna',
								},
								{
									'title': 'Banco de Sangre',
									'desc': '',
								},
							]
						},
					'banco':
						{
							'title': 'Banco de Sangre',
							'desc': 'En nuestro Hospital de Trauma es vital contar con banco de sangre para salvar vidas, la mayoría de nuestros pacientes llega a causa de accidentes, emergencias o enfermedades que provocan pérdidas significativas de sangre por lo que es necesario poder reponerla de inmediato.<br>La donación de sangre es voluntaria.',
							'slogan': '¡Súmate a los héroes anónimos que donan sangre y regalan vida!',
							'link': 'Consulta los requisitos para donar sangre (pdf)',
							'href': '/static/pdf/Requisitos_Donar_Sangre_esp.pdf',
							'link_title': 'Consulta los requisitos para donar sangre (pdf)',
						},
						'preparate': 
						{
							'title': 'Prepárate',
							'href': '/preparate',
							'class': 'terremoto',
							'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
							'pregunta': '¿Qué hacer en caso de...?',
							'tema': 'Terremoto',
							'tema_href': '/preparate/terremoto',
							'tema_respuesta_intro': '¿Estás preparado para un terremoto?',
							'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
							'tema_respuesta_cierre': 'Protege tu hogar contra terremotos.',
							'mas': 'Ayúdanos a prevenir accidentes',
							'mas_href': '/preparate',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'hospital',
							'section_lang': 'the-hospital',
							'has_cycle': 'true',
							'title': 'Hospital'
						},
					'lista_a': 
						[
							'We attend <strong>60%</strong> of trauma services in <strong>Tijuana</strong>.',
							'Made up of<br> <strong>35 doctors  and</strong><br> <strong>45 nurses</strong>',
							'Over <strong>35,000</strong> people attended ',
						],
					'servicios': 
						{
						'title': 'Services',
						'list_a':
							[
								'Emergencies',
								'Hospitalization',
								'Surgery',
								'Resuscitation Room ',
								'Intensive care (pediatric and adults)',
								'Blood Bank',
								'Health Certificate',
								'X-rays and tomography (CT) by Grupo Imagen Radiológica ',
								'Laboratory Tests by Laboratorio Certus ',
							],
						'subtitle': 'Especialized Consultation:',
						'list_b':
							[
								'Traumatology and Orthopedics',
								'Otorhinolaryngology',
								'Cardiology',
								'Psychology ',
								'Neurology',
							],
						},
					'instalaciones':
						{
						'title': 'Hospitalization Area<br> Facilities:',
						'lista':
							[
								{
									'title': 'Emergency Room ',
									'desc': '8 beds',
								},
								{
									'title': 'Resuscitation Room (Red Room) ',
									'desc': '2 beds',
								},
								{
									'title': 'Operating Rooms ',
									'desc': '3 beds',
								},
								{
									'title': 'Hospitalization Area',
									'desc': 'Women  - 4 beds <br>Mens - 13 beds<br>Pediatric  - 4 beds',
								},
								{
									'title': 'Intensive Care ',
									'desc': 'Adults - 4 beds <br>Pediatric - 2 beds',
								},
								{
									'title': 'Semi-Intensive Care Unit ',
									'desc': 'Pediatric - 3 beds',
								},
								{
									'title': 'Thermal Cot ',
									'desc': '1 Cot',
								},
								{
									'title': 'Blood Bank',
									'desc': '',
								},
							]
						},
					'banco':
						{
							'title': 'Blood Bank',
							'desc': 'In our Trauma Hospital it is vital to have a Blood Bank that allows us to save lives, since most of our patients are victims of accidents, emergencies or diseases that cause meaningful blood loss, which makes it necessary to restore the blood immediately. <br> Blood donation is voluntary',
							'slogan': 'Join the nameless heroes that donate blood and give life!',
							'link': 'Learn more of the requirements to donate blood (pdf)',
							'href': '/static/pdf/Requisitos_Donar_Sangre_ing.pdf',
							'link_title': 'Learn more of the requirements to donate blood (pdf)',
						},
					'preparate':
						{
							'title': 'Plan and prepare',
							'href': '/plan-and-prepare',
							'class': 'terremoto',
							'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
							'pregunta': 'What to do in case of…?',
							'tema': 'Earthquakes',
							'tema_href': '/plan-and-prepare/earthquakes',
							'tema_respuesta_intro': 'Are you prepared for a fire?',
							'tema_respuesta_desc': 'This is what you can do to prepare yourself in the event of such emergency.',
							'tema_respuesta_cierre': 'Protect your home from earthquakes.',
							'mas': 'Help us prevent accidents',
							'mas_href': '/plan-and-prepare',
						},
				},
			]		
		return data[lang]

	def ambulance(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'ambulancias',
							'section_lang': 'ambulance',
							'has_cycle': 'true',
							'title': 'Ambulancias',
							'desc': 'Nuestra acción prioritaria es ayudar al más vulnerable y salvar vidas, ofreciendo atención eficiente de servicio prehospitalario y rescate de manera gratuita en casos de emergencia y en situaciones de desastres. Contáctanos a través del 066.',
							'list' :
								[
									'<em>+ 37,000</em> Atendemos más de 37,000 <br>servicios al año.',
									'<em>24 / 7 / 365</em> Todo el año brindamos gratuitamente <br>el servicio de ambulancia y rescate',
									'<em>$ 700 m.n.</em> Cada servicio le cuesta a <br>Cruz Roja $700 pesos',
								],
						},
					'equipo':
						{
							'title': '¿Quiénes conforman la <br>coordinación de socorrismo?',
							'subtitle': 'Conformado por 85 Técnicos en Urgencias Médicas de base (TUMS) y 35 voluntarios TUMS, certificados por Cruz Roja Mexicana:',
							'list': 
								[
									'TUMS Básicos.',
									'TUMS Intermedios.', 
									'Especialistas en rescate en media montaña.',
									'Especialistas en búsqueda y rescate en estructuras colapsadas.',
									'Especialistas en rescate en trincheras.',
									'Especialistas en rescate en ríos.',
									'Rescatistas caninos ',
								],
							'desc': 'La Coordinación de Socorrismo está dirigida a través de radio frecuencia con las siguientes instancias gubernamentales con la misión de unir esfuerzos y continuar salvando vidas: Protección civil, Bomberos y Policía.',
						},
						'articulos_ambulancia':
							{
								'itm1': 'Carro camilla',
								'itm2': 'Férula espinal completa',
								'itm3': 'Mochila de vías aéreas avanzada',
								'itm4': 'Ventilador automático',
								'itm5': 'Mochila de equipo blanco',
								'itm6': '<em>Equipo:</em><ul><li>Oxígeno terapia</li><li>Control de heridas y hemorragias</li><li>Inmovilización de fracturas</li><li>Sueros</li><li>Medicamentos</li><li>Soluciones antisépticas</li></ul>',
								'itm7': 'Oxígeno de base',
								'itm8': '<em>Equipo:</em><ul><li>Collarines cervicales</li><li>Inmovilizadores de cráneo</li><li>Líneas y catéteres de succión</li></ul>',
							},
					'unidades':
						{
							'left':
								{
									'title': 'Equipados con',
									'href': '/ambulancias/equipados',
									'list':
										[
											'<strong>Centro de mando </strong>Con equipo de radiocomunicación.',
											'<strong>Localizador satelital </strong> Todas las unidades tienen localizador satelital que permite ver en tiempo real su ubicación y conocer el historial de rutas. <br><br>Servicio donado por Monsat',
										]
								},
							'right':
								{
									'title': 'Unidades',
									'href': '/ambulancias/unidades',
									'list': [ 'Rescate', 'Ambulancias', 'Supervisión',],
								},
						},
					'listado': 
						{
							'title': 'Ver listado completo de unidades 2013',
							'list_a':
								{
									'title': 'Ambulancias',
									'items':
										[
											{
												'title': '<strong>7</strong>  Volkswagen Crafter',
												'children':
													[
														'<strong>2</strong> unidades 2009',
														'<strong>2</strong> unidades 2010',
														'<strong>2</strong> unidades 2011',
														'<strong>1</strong> unidades 2012',
													],
											},
											{
												'title': '<strong>2</strong> Mercedes Benz Sprinter 2007'
											},
											{
												'title': '<strong>6</strong> Ford Econoline',
												'children':
													[
														'<strong>3</strong> unidades 2006',
														'<strong>1</strong> unidade 2007',
														'<strong>2</strong> unidades 2012',
													],
											},
											{
												'title': '<strong>2</strong>  Peugeot Manager 2012',
											},
										]
								},
							'list_b':
								{
									'title': 'Rescate',
									'items':
										[
											{
												'title': '<strong>1</strong> unidad de rescate especializado',
												'children':
													[
														'Chevrolet Kodiak 2008',
													]
											},
											{
												'title': '<strong>1</strong> unidad de rescate urbano',
												'children':
													[
														'Ford F-350 2001',
													],
											},
											{
												'title': '<strong>1</strong> remolque de emergencias masivas',
											},
											{
												'title': '<strong>1</strong> remolque de rescate urbano',
											},
										]
								},
							'list_c':
								{
									'title': 'Supervisión',
									'items':
										[
											{
												'title': '<strong>2</strong> unidades de supervisión',
												'children':
													[
														'Chevrolet Silverado 2011',
													]
											},
											{
												'title': '<strong>2</strong> unidades de supervisión Ford 1998'
											},
										]
								},
						},
					'bases':
						{
							'title': 'Bases estratégicas',
							'list':
								[
									'Calle 11',
									'Florido',
									'Refugio',
									'Playas de Tijuana',
									'El Dorado',
									'Santa Fe',
									'Mesa de Otay',
									'Base Central',
								],
							'subtitle': 'Nuestras bases de ambulancias, no cuentan con atención médica.',
							'alt': 'Bases de ambulancias',
						},
						'preparate': 
						{
							'title': 'Prepárate',
							'href': '/preparate',
							'class': 'quemaduras',
							'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
							'pregunta': '¿Qué hacer en caso de...?',
							'tema': 'Quemaduras',
							'tema_href': '/preparate/quemaduras',
							'tema_respuesta_intro': '¿Estás preparado para una quemadura?',
							'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
							'tema_respuesta_cierre': 'Protégete y protege a tu familia  contra quemaduras.',
							'mas': 'Ayúdanos a prevenir accidentes',
							'mas_href': '/preparate',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'ambulance',
							'section_lang': 'ambulancias',
							'has_cycle': 'true',
							'title': 'Ambulance Services',
							'desc': 'Our imperative action is to help the most vulnerable, save lives by offering efficient pre-hospitalization services and rescue free of charge in emergency cases and disaster situations. Contact us dialing 066.',
							'list' :
								[
									'<em>+ 37,000</em> We assist over 37,000<br> services per year.',
									'<em>24 / 7 / 365</em> All year long we offer ambulance and rescue services free of charge ',
									'<em>$ 700 pesos</em> Each service costs $700 pesos to the Red Cross',
								],
						},
					'equipo':
						{
							'title': 'Who are the people of the Emergency Services Coordination?',
							'subtitle': 'This Coordination is integrated by 85 Medical Emergency Technicians in station (TUMS by its initials in Spanish) and 35 TUMS volunteers certified by the Mexican Red Cross.',
							'list': 
								[
									'Basic TUMS.',
									'Intermediate TUMS.', 
									'Middle Mountain Region Rescue Specalists.',
									'Collapsed Structures Search and Rescue Specialists.',
									'Trench Rescue Specialists.',
									'River Rescue Specialists.',
									'Canine Agents',
								],
							'desc': 'The First Aid Coordination is directed via radio frequency with the following government agencies: Civil Protection, Fire and Police. Our mission is to unite efforts and keep saving lives.',
						},
						'articulos_ambulancia':
							{
								'itm1': 'Stretcher',
								'itm2': 'Complete spine splint',
								'itm3': 'Advanced airway medical pack',
								'itm4': 'Automatic ventilator',
								'itm5': 'Emergency equipment pack',
								'itm6': '<em>Equipment:</em><ul><li>Therapy oxygen</li><li>Wound and hemorrhage control</li><li>Fracture immobilization</li><li>Serum</li><li>Medicine</li><li>Antiseptic solutions</li></ul>',
								'itm7': 'Oxygen tank',
								'itm8': '<em>Equipment:</em><ul><li>Cervical collar</li><li>Head immobilizer</li><li>Suction catheters and lines</li></ul>',
							},
					'unidades':
						{
							'left':
								{
									'title': 'Equipped with',
									'href': '/ambulance/equipped',
									'list':
										[
											'<strong>Command center </strong>With radio equipment.',
											'<strong>Satellite GPS (Global Positioning System) </strong> All mobile units have a satellite GPS that allows us to see their location in real time and to know their routes history. <br><br>Service donated by Monsat',
										]
								},
							'right':
								{
									'title': 'Units',
									'href': '/ambulance/units',
									'list': [ 'Rescue', 'Ambulances', 'Supervision',],
								},
						},
					'listado': 
						{
							'title': 'See full list of units 2013',
							'list_a':
								{
									'title': 'Ambulances',
									'items':
										[
											{
												'title': '<strong>7</strong>  Volkswagen Crafter',
												'children':
													[
														'<strong>2</strong>- 2009 units',
														'<strong>2</strong>- 2010 units',
														'<strong>2</strong>- 2011 units',
														'<strong>1</strong>- 2012 unit',
													],
											},
											{
												'title': '<strong>2</strong> 2007 Mercedes-Benz Sprinter units '
											},
											{
												'title': '<strong>6</strong> Ford Econoline',
												'children':
													[
														'<strong>3</strong> 2006 units',
														'<strong>1</strong> 2007 unit',
														'<strong>2</strong> 2012 units',
													],
											},
											{
												'title': '<strong>2</strong> 2012 Peugeot Manager units',
											},
										]
								},
							'list_b':
								{
									'title': 'Rescue',
									'items':
										[
											{
												'title': '<strong>1</strong> - Specialized Rescue unit ',
												'children':
													[
														'2008 Chevrolet Kodiak',
													]
											},
											{
												'title': '<strong>1</strong> Urban Rescue unit',
												'children':
													[
														'2001 Ford F-350',
													],
											},
											{
												'title': '<strong>1</strong> Massive Emergency Trailer',
											},
											{
												'title': '<strong>1</strong> Urban Rescue Trailer',
											},
										]
								},
							'list_c':
								{
									'title': 'Supervision',
									'items':
										[
											{
												'title': '<strong>2</strong> Supervision units',
												'children':
													[
														' 2011 Chevrolet Silverado',
													]
											},
											{
												'title': '<strong>2</strong> Supervision 1998 Ford units'
											},
										]
								},
						},
					'bases':
						{
							'title': 'Strategic Ambulance Stations',
							'list':
								[
									'11th Street',
									'Florido',
									'Refugio',
									'Playas de Tijuana / Tijuana Beach',
									'El Dorado',
									'Santa Fe',
									'Mesa de Otay / Otay Mesa',
									'Headquarters',
								],
							'subtitle': 'Our stations do not provide medical attention.',
							'alt': 'Ambulance Stations',
						},
					'preparate':
						{
							'title': 'Plan and prepare',
							'href': '/plan-and-prepare',
							'class': 'quemaduras',
							'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
							'pregunta': 'What to do in case of…?',
							'tema': 'Burns',
							'tema_href': '/plan-and-prepare/burns',
							'tema_respuesta_intro': 'Are you prepared for a fire?',
							'tema_respuesta_desc': 'This is what you can do to prepare yourself in the event of such emergency.',
							'tema_respuesta_cierre': 'Protect yourself and your family from burns',
							'mas': 'Help us prevent accidents',
							'mas_href': '/plan-and-prepare',
						},
				},
			]		
		return data[lang]

	def donations(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'donativos',
							'section_lang': 'donations',
							'has_cycle': 'true',
							'title': '<span class="hidden">Donativos.</span> Dona Ahora',
							'tipo': 
								[
									{
										'id': 'don_dinero',
										'href': '/donativos/programa-benefactor-distinguido',
										'title': 'Dinero'
									},
									{
										'id': 'don_tiempo',
										'href': '/donativos/tiempo',
										'title': 'Tiempo'
									},
									{
										'id': 'don_especie',
										'href': '/donativos/especie',
										'title': 'Especie'
									},
								],
							'slogan': '<strong>Importante:</strong> Los donativos son <br>deducibles de impuestos.',
						},
					'submenu':
						[
							{
								'id': '',
								'href': '/donativos/programa-benefactor-distinguido',
								'title': 'Programa de<br> benefactor distinguido',
								'alt': 'Programa de benefactor distinguido',
							},
							{
								'id': 'donat_linea',
								'href': '/donativos/linea',
								'title': 'Donaciones <br>en línea',
								'alt': 'Donaciones en línea',
							},
							{
								'id': 'donat_cuenta',
								'href': '/donativos/deposito-cuenta-bancaria',
								'title': 'Depósito directo en<br> cuenta bancaria',
								'alt': 'Depósito directo en cuenta bancaria',
							},
							{
								'id': 'donat_voluntariado',
								'href': 'mailto:recursoshumanos@cruzrojatijuana.org.mx',
								'title': 'Voluntariado',
								'alt': 'Voluntariado',
							},
							{
								'id': 'donat_especie',
								'href': '/donativos/especie',
								'title': 'Donativos en especie',
								'alt': 'Donativos en especie',
							},
						],
					'programa':
						{
							'title': 'Programa de Benefactor Distinguido.',
							'desc': 'Por medio de domiciliación. <br>Autoriza un cargo fijo mensual en moneda nacional a tu tarjeta de crédito, tarjeta de débito o cuenta de cheques.',
							'list': 
								[
									'Llena el formato de domiciliación, fírmalo y Cruz Roja realizará el cargo mensual.', 
									'Donativo constante en especie.', 
									'Un programa 100% seguro.'
								],
							'desc_b': 'Comienza ahora, descarga el formato de domiciliación.',
							'link':
								{
									'href': '/static/pdf/Formato-Domiciliacion.pdf',
									'alt': 'Descarga formato de domiciliación',
									'title': 'Descarga formato',
								},
						},
					'donacion':
						{
							'title': 'Donaciones en línea',
							'subtitle': 'Realiza tu donación a través del sistema PayPal.',
							'desc': 'Para realizar donaciones en línea a través del sistema PayPal haz click en el siguiente botón:',
							'paypal':
								{
									'title': 'Paypal',
									'href': 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5NL5HVNJCGK24',
									'alt': 'Donar por medio de Paypal',
								},
							'icf':
								{
									'title': 'Realiza tu donación por medio de International Community Foundation.',
									'list': 
										[
											{'title': 'Deducible para IRS'},
											{
												'title': 'Programa donativo:',
												'children': ['Mensual', 'Anual', 'Único'], 
											},
										],
								},
							'alt_text': 'Visita la página oficial, directamente a la sección de Cruz Roja Tijuana',
							'link': 
								{
									'href': '',
									'alt': '',
									'title': '',
								},
							'link_b':
								{
									'href': 'http://www.icfexchange.org/donateonline/index.php?webkey=cruzrojatijuana',
									'alt': 'International Community Foundation',
									'title': 'Donar',
								},
						},
					'deposito':
						{
							'title': 'Depósito directo en cuentas bancarias',
							'mx':
								{
									'title': 'México',
									'banco': 'Banco: BBVA Bancomer<br>Nombre: Cruz Roja Mexicana. IAP',
									'cuentas':
										[
											{
												'title': 'Moneda Nacional:',
												'datos': 'Cuenta: 01024328892<br>Clabe: 012028001024328892',
											},
											{
												'title': 'Dólares:',
												'datos': 'Cuenta: 0100825948<br>Clabe: 012028001008259482'
											},
										],
								},
							'us':
								{
									'title': 'Estados Unidos',
									'banco': 'Banco: Bank of America<br>Nombre: Cruz Roja Mexicana',
									'cuenta': 'Cuenta: 2184210669<br>Swift: BOFAUS3N<br>ABA: 026009593',
								}
						},
					'voluntariado':
						{
							'title': 'Voluntariado',
							'desc': 'La creación del movimiento Internacional de Cruz Roja tiene el objetivo de encausar a niños, jóvenes y adultos hacia el trabajo comunitario conforme a la filosofía Institucional de los Siete Principios para impulsar el cumplimiento de nuestra misión.',
							'beneficios':
								{
									'title': 'Beneficios',
									'list': ['Capacitación.', 'Formación y crecimiento humano.', '<strong>Servicio social.</strong>', '<strong>Prácticas profesionales.</strong>'],
									'slogan': '¡Súmate al movimiento más grande el mundo!',
								},
							'ayuda':
								{
									'title': 'Ayúdanos a ayudar"',
									'link':
										{
											'title': 'Súmate',
											'href': '/contacto',
											'alt': 'Únete a nuestros voluntarios',
										},
									'contacto': 'Contáctanos',
									'depto': 'Recursos Humanos.',
									'tel': '(664) 608.67.09',
									'link_b':
										{
											'title': 'recursoshumanos@cruzrojatijuana.org.mx',
											'href': 'mailto:recursoshumanos@cruzrojatijuana.org.mx',
											'alt': 'Contacta al departamento de recursos humanos',
										},
								},
						},
					'especie':
						{
							'title': 'Donativos en especie',
							'list': [ 'Donación de sangre', 'Chatarra de metal', 'Equipo médico y medicamento', 'Asesoría profesional', 'Espacios publicitarios', 'Alimentos', 'Donativo en especie', 'Diesel y gasolina', 'Blancos, etc' ],
							'contacto':
								{
									'title': 'Contáctanos',
									'link':
										{
											'href': '/contacto',
											'alt': 'Contacta al departamento de procuración',
											'title': 'Contáctanos'
										},
									'desc': 'Procuración de Fondos.',
									'tel': '(664) 608.67.27',
								},
						},
					'benefactores':
						{
							'title': 'Benefactores',
							'list':
								[
									{
										'href': '#',
										'alt': 'Visita a nuestro patrocinador',
										'id': 'benef_coca',
										'title': 'Coca cola',
									},
									{
										'href': '#',
										'alt': 'Visita a nuestro patrocinador',
										'id': 'benef_xolos',
										'title': 'Xolos',
									},
									{
										'href': '#',
										'alt': 'Visita a nuestro patrocinador',
										'id': 'benef_honda',
										'title': 'Honda',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_xolos',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_honda',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_honda',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_honda',
										'title': '',
									},
								]
						},
						'preparate': 
						{
							'title': 'Prepárate',
							'href': '/preparate',
							'class': 'fracturas',
							'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
							'pregunta': '¿Qué hacer en caso de...?',
							'tema': 'Fracturas',
							'tema_href': '/preparate/fracturas',
							'tema_respuesta_intro': '¿Estás preparado para una fractura?',
							'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
							'tema_respuesta_cierre': 'Protégete y protege a tu familia contra fracturas.',
							'mas': 'Ayúdanos a prevenir accidentes',
							'mas_href': '/preparate',
						},
				},				
				{#ENGLISH					
					
					'gral_info': 
						{ 							
							'section': 'donativos',
							'section_lang': 'donations',
							'has_cycle': 'true',
							'title': '<span class="hidden">Donation.</span> How to donate',
							'tipo': 
								[
									{
										'id': 'don_dinero',
										'href': '/donations/distinguished-benefactor-program',
										'title': 'Money'
									},
									{
										'id': 'don_tiempo',
										'href': '/donations/time',
										'title': 'Time'
									},
									{
										'id': 'don_especie',
										'href': '/donations/kind',
										'title': 'In Kind'
									},
								],
							'slogan': '<strong>Important:</strong> Los donativos son <br>deducibles de impuestos.',
						},
					'submenu':
						[
							{
								'id': '',
								'href': '/donations/distinguished-benefactor-program',
								'title': 'Distinguished<br /> Benefactor program.',
								'alt': 'Distinguished Benefactor program.',
							},
							{
								'id': 'donat_linea',
								'href': '/donations/money',
								'title': 'On Line<br /> Donation',
								'alt': 'On Line Donation',
							},
							{
								'id': 'donat_cuenta',
								'href': '/donativos/bank-account-deposit',
								'title': 'Bank Account<br /> Deposit',
								'alt': 'Bank Account Deposit',
							},
							{
								'id': 'donat_voluntariado',
								'href': 'mailto:recursoshumanos@cruzrojatijuana.org.mx',
								'title': 'Voluntary Service',
								'alt': 'Voluntary Service',
							},
							{
								'id': 'donat_especie',
								'href': '/donations/kind',
								'title': 'Donations in Kind ',
								'alt': 'Donations in Kind ',
							},
						],
					'programa':
						{
							'title': 'Distinguished Benefactor program.',
							'desc': 'Through direct billing. . <br>Authorizes a monthly payment in national currency to your credit card, debit card or check account.',
							'list': 
								[
									'Fill the direct billing form, sign it and the Red Cross will make the monthly charge. ', 
									'Constant donation in kind ', 
									'A 100% safe program'
								],
							'desc_b': 'Start now, download the direct billing form',
							'link':
								{
									'href': '/static/pdf/Formato-Domiciliacion.pdf',
									'alt': 'Download the direct billing form',
									'title': 'Download form',
								},
						},
					'donacion':
						{
							'title': 'On Line Donation',
							'subtitle': 'Donate through the PayPal system',
							'desc': 'To donate through PayPal click ‘donate’.',
							'paypal':
								{
									'title': 'Paypal',
									'href': 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5NL5HVNJCGK24',
									'alt': 'Donate trough Paypal',
								},
							'icf':
								{
									'title': 'Make your donation through the International Community Foundation ',
									'list': 
										[
											{'title': 'IRS deductible'},
											{
												'title': 'Donation program:',
												'children': ['Monthly', 'Annual', 'Only Once'], 
											},
										],
								},
							'alt_text': '',
							'link': 
								{
									'href': '',
									'alt': '',
									'title': '',
								},
							'link_b':
								{
									'href': 'http://www.icfexchange.org/donateonline/index.php?webkey=cruzrojatijuana',
									'alt': 'International Community Foundation',
									'title': 'Donate',
								},
						},
					'deposito':
						{
							'title': 'Bank Account Deposit',
							'mx':
								{
									'title': 'México',
									'banco': 'Bank: BBVA Bancomer<br>Name: Cruz Roja Mexicana. IAP',
									'cuentas':
										[
											{
												'title': 'National Currency: (Mexican Pesos)',
												'datos': 'Account: 01024328892<br>Clabe: 012028001024328892',
											},
											{
												'title': 'Dollars:',
												'datos': 'Account: 0100825948<br>Clabe: 012028001008259482'
											},
										],
								},
							'us':
								{
									'title': 'San Diego',
									'banco': 'Bank: Bank of America<br>Name: Cruz Roja Mexicana',
									'cuenta': 'Account: 2184210669<br>Swift: BOFAUS3N<br>ABA: 026009593',
								}
						},
					'voluntariado':
						{
							'title': 'Voluntary Service',
							'desc': 'The creation of the Red Cross movement has the objective of promoting volunteer work among children, teenagers, and adults, in accordance to the Institutional philosophy of the Fundamental Principles to motivate the fulfillment of our mission.  ',
							'beneficios':
								{
									'title': 'Benefits',
									'list': ['Training.', 'Education and human growth', '<strong>Social Service</strong>', '<strong>Professional Practice</strong>'],
									'slogan': 'Join the Largest Movement in the World!',
								},
							'ayuda':
								{
									'title': ' Help Us Help"',
									'link':
										{
											'title': 'Join Us',
											'href': '/contact',
											'alt': 'Únete a nuestros voluntarios',
										},
									'contacto': 'Contact us',
									'depto': 'Human resources.',
									'tel': '(664) 608.67.09',
									'link_b':
										{
											'title': 'recursoshumanos@cruzrojatijuana.org.mx',
											'href': 'mailto:recursoshumanos@cruzrojatijuana.org.mx',
											'alt': 'Contact the human resources department',
										},
								},
						},
					'especie':
						{
							'title': 'Donations In-Kind',
							'list': [ 'Blood Donation', 'Metal Scrap', 'Medical Equipment and Medicines', 'Professional Assistance', 'Advertising Spaces', 'Food', 'Donation In Kind ', 'Diesel and gas (fuel)', 'Appliances, etc' ],
							'contacto':
								{
									'title': 'Learn More',
									'link':
										{
											'href': '/contact',
											'alt': 'Contact our fundraising department',
											'title': 'Contact Us'
										},
									'desc': 'Fundraising department.',
									'tel': '(664) 608.67.27',
								},
						},
					'benefactores':
						{
							'title': 'Benefactores',
							'list':
								[
									{
										'href': '#',
										'alt': 'Visita a nuestro patrocinador',
										'id': 'benef_coca',
										'title': 'Coca cola',
									},
									{
										'href': '#',
										'alt': 'Visita a nuestro patrocinador',
										'id': 'benef_xolos',
										'title': 'Xolos',
									},
									{
										'href': '#',
										'alt': 'Visita a nuestro patrocinador',
										'id': 'benef_honda',
										'title': 'Honda',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_xolos',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_honda',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_honda',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': '',
										'title': '',
									},
									{
										'href': '#',
										'alt': '',
										'id': 'benef_honda',
										'title': '',
									},
								]
						},
					'preparate':
						{
							'title': 'Plan and prepare',
							'href': '/plan-and-prepare',
							'class': 'fracturas',
							'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
							'pregunta': 'What to do in case of…?',
							'tema': 'Fractures',
							'tema_href': '/plan-and-prepare/fractures',
							'tema_respuesta_intro': 'Are you prepared for a fire?',
							'tema_respuesta_desc': 'This is what you can do to prepare yourself in the event of such emergency.',
							'tema_respuesta_cierre': 'Protect yourself and your family from Fractures.',
							'mas': 'Help us prevent accidents',
							'mas_href': '/plan-and-prepare',
						},
				},
			]		
		return data[lang]

	def transparency(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'transparencia',
							'section_lang': 'transparency',
							'has_cycle': 'true',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'transparencia',
							'section_lang': 'transparency',
							'has_cycle': 'true',
						},
				},
			]		
		return data[lang]

	def contact(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'contacto',
							'section_lang': 'contact',
							'has_cycle': 'true',
						},
						'preparate': 
						{
							'title': 'Prepárate',
							'href': '/preparate',
							'class': 'envenenamiento',
							'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
							'pregunta': '¿Qué hacer en caso de...?',
							'tema': 'Envenenamiento',
							'tema_href': '/preparate/envenenamiento',
							'tema_respuesta_intro': '¿Estás preparado para un envenenamiento?',
							'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
							'tema_respuesta_cierre': 'Protégete y protege a tu familia contra envenenamientos',
							'mas': 'Ayúdanos a prevenir accidentes',
							'mas_href': '/preparate',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'contacto',
							'section_lang': 'contact',
							'has_cycle': 'true',
						},
					'preparate':
						{
							'title': 'Plan and prepare',
							'href': '/plan-and-prepare',
							'class': 'envenenamiento',
							'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
							'pregunta': 'What to do in case of…?',
							'tema': 'Poisoning',
							'tema_href': '/plan-and-prepare/poisoning',
							'tema_respuesta_intro': 'Are you prepared for a fire?',
							'tema_respuesta_desc': 'This is what you can do to prepare yourself in the event of such emergency.',
							'tema_respuesta_cierre': 'Protect your home from fires poisoning',
							'mas': 'Help us prevent accidents',
							'mas_href': '/plan-and-prepare',
						},
				},
			]		
		return data[lang]
		
		

	def news(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'noticias',
							'section_lang': 'news',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'noticias',
							'section_lang': 'news',
						},
				},
			]		
		return data[lang]

	def training_center(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'centro-capacitacion',
							'section_lang': 'training-center',
							'page_title': 'Noticias',
						},
					'preparate': 
						{
							'title': 'Prepárate',
							'href': '/preparate',
							'class': 'ataque-corazon',
							'desc': 'Aprende con nosotros y ayúdanos a promover la capacitación y cultura de prevención para salvar vidas en situaciones de emergencia y desastres.',
							'pregunta': '¿Qué hacer en caso de...?',
							'tema': 'Ataque al corazón',
							'tema_href': '/preparate/ataque-corazon',
							'tema_respuesta_intro': '¿Estás preparado para un ataque al corazón?',
							'tema_respuesta_desc': 'Esto es lo que puedes hacer para preparate en caso de tal emergencia.',
							'tema_respuesta_cierre': 'Protege tu hogar contra ataques al corazón',
							'mas': 'Ayúdanos a prevenir accidentes',
							'mas_href': '/preparate',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'centro-capacitacion',
							'section_lang': 'training-center',
							'page_title': 'News',
						},
					'preparate':
						{
							'title': 'Plan and prepare',
							'href': '/plan-and-prepare',
							'desc': 'Come learn with us. Help us promote a culture of prevention through trainings to save lives in case of emergencies and disasters.',
							'pregunta': 'What to do in case of…?',
							'tema': 'Heart Attack',
							'tema_href': '/plan-and-prepare/heart-attack',
							'tema_respuesta_intro': 'Are you prepared for a fire?',
							'tema_respuesta_desc': 'This is what you can do to prepare yourself in the event of such emergency.',
							'tema_respuesta_cierre': 'Protect your home from fires heart attack',
							'mas': 'Help us prevent accidents',
							'mas_href': '/plan-and-prepare',
						},
				},
			]		
		return data[lang]
		
	def preparate(self, lang):
		data = [
				{#SPANISH					
					'gral_info': 
						{ 							
							'section': 'preparate',
							'section_lang': 'plan-and-prepare',
						},
				},				
				{#ENGLISH					
					'gral_info': 
						{ 							
							'section': 'preparate',
							'section_lang': 'plan-and-prepare',
						},
				},
			]		
		return data[lang]
