var folder = '/';
var server = extras.get_server_path() + folder;

$(window).load(function(){
	var page = extras.get_currentpage();
	var last_item = extras.getLastItem(page)

	extras.turon_page('wrapper')
	hide_menu()
	donations_stick()

	if($('.inicio').length){ index_scrolled() }

	if($('#scroll_down').length){ index_scroll_down() }


	if('#donations_menu'.length){ donations_menu() }

	if($('#wrapper.inicio').length){
		
		$('#header, #intro_general .background').hide();
		$('#first_p, #index_news, #social_block').hide();
		$('#ambulancia h2, #ambulancia hr, #ind_phone, #ind_ambulance, #ind_hospital').hide();
		$('#acceso_transparencia_wrapp').hide();
		$('#como-donar h2').hide();
		$('#col_animada_especie h3, #col_animada_especie hr, #col_animada_especie ul, #mini_col_animada_especie, #col_animada_tiempo h3 , #col_animada_tiempo hr, #col_animada_tiempo ul, #mini_col_animada_tiempo, #col_animada_dinero h3, #col_animada_dinero hr, #col_animada_dinero p, #mini_col_animada_dinero').hide();
		
		

		// INICIA ANIMACIONES

			// call waypoint plugin

			// Encabezado
			$('#header').waypoint(function(event, direction) {
			    // do your fade in here
			    $('#header').fadeIn(2500);
			    $('#intro_general .background').fadeIn(2500);
			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') - $(this).outerHeight();
			    }
			});

			// Bloque de bienvenida, inicio
			$('#index_news').waypoint(function(event, direction) {
			    // do your fade in here
			    $('#index_news, #social_block').fadeIn(1600);
			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') - $(this).outerHeight();
			    }
			});
			$('#img_conocer').waypoint(function(event, direction) {
			    // do your fade in here
			    $('#img_conocer, #img_donar, #img_slideshow').addClass("animated");
			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') - 100;
			    }
			});

			

			// Bloque azul, inicio
			$('.inicio .blue_container').waypoint(function(event, direction) {
			    // do your fade in here
			    $('.inicio .blue_container').addClass("inview"); 
					$('#ambulancia hr').fadeIn(1200);
					$('#ambulancia h2').delay( 200 ).fadeIn(1200);
					$('#ind_phone').delay( 900 ).fadeIn(1200);
					$('#ind_ambulance').delay( 1800 ).fadeIn(1200);
					$('#ind_hospital').delay( 2500 ).fadeIn(1200);
					$('#ambulancia hr').delay( 3000 ).fadeIn(1200);

			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') -200;
			    }
			});

				// Bloque azul texto, inicio
				$('#bloque_socorrismo').waypoint(function(event, direction) {
				    // do your fade in here
				    $('#bloque_socorrismo').delay( 4000 ).addClass("fadeInLeft"); 
						$('#bloque_hospital').delay( 5200 ).addClass("fadeInLeft"); 
						$('#boton_hospital').delay( 6200 ).addClass("fadeInLeft");
						

				}, {
				   offset: function() {
				       // The bottom of the element is in view
				       return $.waypoints('viewportHeight') -300;
				    }
				});

			// Bloque azul texto, inicio
			$('#bloque_cap').waypoint(function(event, direction) {
			    // do your fade in here
			    $('#bloque_cap').addClass("fadeInLeft"); 
					$('#capacitacion_img').delay( 2000 ).addClass("fadeInLeft");

			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') -100;
			    }
			});

			// Transparencia, inicio
			$('#img_donativos_cuotas').waypoint(function(event, direction) {
			    // do your fade in here
			    $('#img_donativos_cuotas').addClass("fadeInLeft"); 
					$('#acceso_transparencia_wrapp').delay( 500 ).fadeIn(1200);
			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') -100;
			    }
			});

			// Logros, inicio
			$('#bloque_logros_index').waypoint(function(event, direction) {
			    // do your fade in here

			    $('#bloque_logros_index').delay( 400 ).addClass("fadeInDown");

			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') - 100;
			    }
			});


			// Donaciones, inicio
			$('#como-donar').waypoint(function(event, direction) {
			    // do your fade in here

			    $('#como-donar').addClass("inview");
					$('#como-donar h2').delay( 200 ).fadeIn(1200);
					
					
					$('#col_animada_especie h3, #col_animada_especie hr').delay( 1200 ).fadeIn(1200);
					$('#col_animada_especie ul').delay( 1800 ).fadeIn(1200);
					$('#mini_col_animada_especie').delay( 2400 ).fadeIn(1200);
					
					
					$('#col_animada_tiempo h3, #col_animada_tiempo hr').delay( 2800 ).fadeIn(1200);
					$('#col_animada_tiempo ul').delay( 3200 ).fadeIn(1200);
					$('#mini_col_animada_tiempo').delay( 3600 ).fadeIn(1200);
					
					
					$('#col_animada_dinero h3, #col_animada_dinero hr').delay( 4000 ).fadeIn(1200);
					$('#col_animada_dinero p').delay( 4400 ).fadeIn(1200);
					$('#mini_col_animada_dinero').delay( 4800 ).fadeIn(1200);


			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') - 100;
			    }
			});


			// Donaciones, inicio
			$('.inicio #preparate_videos').waypoint(function(event, direction) {
			    // do your fade in here
			    $('.inicio #preparate_videos, #footer.inicio').delay( 400 ).addClass("fadeInDown");

			}, {
			   offset: function() {
			       // The bottom of the element is in view
			       return $.waypoints('viewportHeight') -100;
			    }
			});


		// TERMINA ANIMACIONES
		
	}

	if($('.slider_nav a').length){
		load_mint_sliders()
	}
	

	if($('#img_slideshow').length)
	{
		load_cycle_slider('fade')	
		load_campanas_fancybox()
	}

	if($('#'+last_item).length) extras.gotoTop(last_item)

	if($('.slider_news').length) load_news()
	
	if($('.slider_vert').length) load_vertical_slider()

	if($('.second_slider').length) load_second_slider()

	if($('.slider_horz').length) load_vertical_horz()
		
	if($('#twitter_panel').length) get_last_tweets()
	
	if($('#video_wrapp').length) load_youtube_video()
	
	if($('#donativos').length) load_logros()
	
	if($('#timeline').length) load_timeline()
	
	if($('#bot_listado_unidades h2').length) load_blink_area()
	
	if($('#directorio_acordeon').length) load_acordeon()
	
	if($('#lista_elementos').length) ambulance_tools()
	
	//if($('#map_nav').length) contact_map()

	if($('#transparencia_menu').length) load_transparencia();

	if($('#preparate_menu').length) load_preparate();

	if($('.breadcrumb').length) check_breadcrumb()
	
	if($('#slider_bases').length) ambulance_slide()
	
	if($('#creditos').length) load_creditos();

	if($('#intro_contacto').length) gmap_initialize();

	//if($('#intro_contacto').length) load_g_maps(); 

	if($('#contact_form').length) load_contact_form();

	if($('#nav_bases').length) load_slide_bases();

	if($('#intro_donativos').length) load_donativos();

})
function donations_menu()
{
	$('#donations_menu li a').click(function(){	
		
		if($(this).parent().attr('id') == "donat_voluntariado"){
		
		}
		else{
		
			var url_tmp = $(this).attr("href");
			var new_url= url_tmp.substr(url_tmp.lastIndexOf('/') + 1);
			$('html, body').animate({scrollTop:$('#'+new_url).offset().top - 55}, 'slow');

			return false;
		}
		
	})
}

function index_scroll_down()
{
	$('#scroll_down').click(function(){	
		$('html, body').animate({scrollTop:$('#dark_intro_block').offset().top - 55}, 'slow')
	})
	
}


function index_scrolled()
{
	var $document = $(document),
	    $element = $('#index_about'),
	    className = 'fixed',
	    className2 = 'hidden';

	$document.scroll(function() {
	  if ($document.scrollTop() >= 183) {
	    // user scrolled 183 pixels or more;
	    // do stuff
	    $element.addClass(className);
	  } else {
	    $element.removeClass(className);
	  }
		
		if ($document.scrollTop() >= 1500) {
	    $element.removeClass(className);
			$element.addClass(className2);
		}	else {
		    $element.removeClass(className2);
		  }
	});
}


function load_donativos()
{
	$('#intro_donativos a').click(function(){
		var tag = $(this).attr('href')

		last_item = extras.getLastItem(tag)
		extras.gotoTop(last_item)
		var active_lang = $('#lang').find('.active');
		//var lang = $(active_lang).text() == 'Esp' ? 0:1;
		if($(active_lang).text() == 'Esp')
			extras.update_path( '/donativos/' + last_item);
		else
			extras.update_path( '/donations/' + last_item);
		return false;
	})
}

function load_slide_bases()
{
	$('#nav a').click(function(){
		var id = $(this).text()
		$('#nav_bases').find('.active').removeClass('active')
		$('#li_'+id).addClass('active')
	});
}

function load_contact_form()
{
	$('#contact_form').submit(function()
	{
		var flag = true;
		var tags = new Array('name', 'email', 'message');
		var active_lang = $('#lang').find('.active');
		var lang = $(active_lang).text() == 'Esp' ? 0:1;
		var msg_fill_fields = new Array('Favor de llenar campos marcados en rojo', 'Plase fill all fields in red');
		var msg_valid_email = new Array('Favor de captura un email correcto.', 'Please put a valid email.');
		var msg_sending = new Array('Enviando mensaje, Favor espera...', 'Sending message, please waite...');
		var msg_success = new Array('Mensaje enviado correctamente, gracias.', 'Your message has been sent, thank you.');
		var msg_error = new Array('Lo sentimos el mensaje no se pudo enviar, <br />favor de intetar mas tarde.', 'We are sorry, the message could not been sent, <br />please try later.');
		for(i=0; i<tags.length; i++)
		{
			if($('#'+tags[i]).val() == '')
			{
				flag = false;
				$('#'+tags[i]).prev().addClass('required');
			}
			else $('#'+tags[i]).prev().removeClass('required');
		}
		if(!flag) $('#msg').html(msg_fill_fields[lang]);
		else
		{
			if(!is_email($('#email').val())) $('#msg').html(msg_fill_fields[lang]);
			else
			{
				$('#msg').html(msg_sending[lang]);
				$.post("send_mail_form", $("#contact_form").serialize(), function(data){
					if(data == 'success')
					{
						$('#msg').html(msg_success[lang]); 
						clear_form('contact_form');
					}
					else if(data == 'empty_data') $('#msg').html(msg_fill_fields[lang]);
					else $('#msg').html(msg_error[lang]);
				})
			}
		}
		return false;
	})
}


/************************************************ STARTS GOOGLE MAPS ************************/
	

function gmap_initialize() {

	var MY_MAPTYPE_ID = 'custom_style';
	var featureOpts = 
	[
		{
			"elementType": "geometry.fill",
			"stylers": 
			[
				{"visibility": "on"},
				{"color": "#dddfe0"},
			],
		},
		{
			"elementType": "labels.text.stroke",
			"stylers" :
			[
				{"visibility": "on"},
				{"color": "#f9f9fd"},
			],
		},
		{
			"elementType": "geometry.stroke",
			"stylers": 
			[
				{"visibility": "on"},
				{"color": "#ed312f"},
				{"weight": 0.3}
			]
		},

	];

	var contentString = 'nice'
	
	var data = new Array();
	data[0] = new google.maps.LatLng(32.506894, -116.963899);
	data[1] = new google.maps.LatLng(32.524947, -117.028196);
	

	var html_popup = [{title: '<div class="infoWindow"><b>Cruz Roja Mexicana Delegación Tijuana</b><br />Alfonso Gamboa esq. Enrique Silvestre s/n, <br />2da. Etapa Zona Río<br /><br />Tel. (664) 608.67.00<br /><br /><a href="http://goo.gl/v0fJxc" title="Cruz Roja Mexicana Delegación Tijuana" target="_blank">Ubicación</a></div>'},{title: '<div class="infoWindow"><b>Centro de capacitación Cruz Roja Mexicana Tijuana</b><br/>Calle 11 No. 8930, Zona Centro.<br />Tel. (664) 687.45.20 , (664) 684.98.26<br /><br /><a href="http://goo.gl/E3wBKK" title="Centro de capacitación Cruz Roja Mexicana Tijuana" target="_blank">Ubicación</a></div>'}];


	var mapOptions = {
		zoom: 13,
		center: data[0],
		mapTypeControlOptions: {
		  mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
		},
		mapTypeId: MY_MAPTYPE_ID,

		//mapTypeControl: false,
		//overviewMapControl: true,
	};
	
	map = new google.maps.Map(document.getElementById('map_delegacion'),
	  mapOptions);

	var bounds = new google.maps.LatLngBounds(data[1], data[0]);
	map.fitBounds(bounds);

	var image = './static/images/google_maps.png';

	for(i=0; i<data.length; i++)
	{
		var marker = new google.maps.Marker({	
			position: data[i],
			map: map,
			icon: image,
		});	
		marker.setTitle(i.toString());
		attachPopup(marker, html_popup[i]);
	}

	var styledMapOptions = {
		name: MY_MAPTYPE_ID
	};

	var customMapType = new google.maps.StyledMapType(featureOpts, styledMapOptions);

	map.mapTypes.set(MY_MAPTYPE_ID, customMapType);
}

function attachPopup(marker, number) {
	var infowindow = new google.maps.InfoWindow({
		content: number.title,
	});
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map,marker);
	});
}

/************************************************ ENDS GOOGLE MAPS ************************/

function load_g_maps()
{
	$('#map_delegacion').html('<iframe width="100%" height="426" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="//maps.google.com/maps/ms?msid=201853418072443998960.0004e337960233a240d98&amp;msa=0&amp;ie=UTF8&amp;t=m&amp;ll=32.529013,-116.982079&amp;spn=0.061655,0.102997&amp;z=13&amp;iwloc=0004e337a3a76a17e8428&amp;output=embed"></iframe>');
}

function load_creditos()
{
	$('#footer .container #sitemap #other_links .first li .fancybox').click(function(){
			$('#creditos').removeClass('invisible').addClass('visible');
			return false;
	});
	$('#creditos #cred_out').click(function(){
			$('#creditos').removeClass('visible').addClass('invisible');
	});
}

function clear_form(form)
{
	$( '#'+form ).each(function(){
	    this.reset();
	});
}
function is_email(email)
{
	var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function ambulance_slide(){
	
	$('#slider_bases').after('<div id="nav" class="bullet_nav">').cycle({ 
	    fx:     'turnDown', 
	    speed:  'fast', 
	    //timeout: 0, 
	    pager:  '#nav',
	    after: function(currSlideElement, nextSlideElement, options, forwardFlag){
	    	id = $(nextSlideElement).attr('class')
	    	$('#nav_bases').find('.active').removeClass('active')
	    	$('#'+id).addClass('active')
	    } 
	});
	
}

function check_breadcrumb()
{
	if($('.breadcrumb').html().length < 20 )
		$('.breadcrumb').addClass('invisible')
}

function load_preparate()
{
	$('#preparate_menu li').click(function(){
		id_tmp = $(this).attr('id');
		id= id_tmp.split("_").pop();
		$('#panel_casos').find('.visible').removeClass('visible').addClass('invisible');
		$('#caso_'+id).addClass('visible').removeClass('invisible');

		tag = $(this).children().attr('href');

		window.history.pushState(tag, tag, tag);
		return false;
	})	
}

function load_transparencia()
{
	$('#transparencia_menu a').click(function(){
		id = $(this).attr('alt')
		href = $(this).attr('href')
		if(id)
		{
			$('#content').find('.visible').removeClass('visible').addClass('invisible')
			$('#'+id).removeClass('invisible').addClass('visible')
			$('#transparencia_menu').find('.current').removeClass('current')
			$(this).parent().addClass('current')
			page = extras.get_currentpage()
			section = extras.getFirstItem(page)
			window.history.pushState('', '', href);
			return false;
		}
	})
}

function load_acordeon()
{
	$("#directorio_acordeon > li > h3").click(function(){
		$('#directorio_acordeon div').slideUp(300);
	    if(false == $(this).next().is(':visible')) {
				
				$('#directorio_acordeon h3').css({'background-position':"right 15px"});
				$('#directorio_acordeon div').hide('slow');
				
				$(this).next().show('slow');
	    	$(this).css({'background-position':"right -37px"});
			
	    }
			else{
				$(this).css({'background-position':"right 15px"});
			}
	});
	$('#directorio_acordeon div:eq(0)').show();
	$('#directorio_acordeon h3:eq(0)').css({'background-position':"right -37px"});
}

function load_blink_area()
{
	$('#bot_listado_unidades h2').click(function(){
		if($('#bloque_listado_unidades').hasClass('close'))
		{
			
			$('#bot_listado_unidades h2').css({'background-image':"url(/static/images/fe/close_symbol.png)"});	$('#bloque_listado_unidades').toggleClass('invisible')
			$('#bloque_listado_unidades').animate({
				height: '473'
			}, 1000, function() {
				$('#bloque_listado_unidades').toggleClass('close')
				
		  	});
		}
		else
		{
			$('#bot_listado_unidades h2').css({'background-image':"url(/static/images/fe/down_arrow.png)"});
			$('#bloque_listado_unidades').animate({
				height: '0'
			}, 1000, function() {
				$('#bloque_listado_unidades').toggleClass('close')
				$('#bloque_listado_unidades').toggleClass('invisible')
				
				
		  	});	
		}
		return false
	})
}

function load_second_slider()
{
	$('.second_slider')	
	.cycle({ 
	    fx:     'scrollVert', 
	    next:   '#second_next', 
    	prev:   '#second_prev', 
    	timeout: 12000    	
	});
}

function load_timeline()
{
	var timeline = new VMM.Timeline();
	if($('.eng').length){
		timeline.init("/static/data/data_en.json");
	}
	else{
		timeline.init("/static/data/data.json");
	}
	
}

function hide_menu()
{
	if($('#hidden_menu').offset())
		var sticky_navigation_offset_top = 680;
		//var sticky_navigation_offset_top = $('#hidden_menu').offset().top;
	var sticky_navigation = function(){
		var scroll_top = $(window).scrollTop();
		scroll_top+=18;
		if (scroll_top > sticky_navigation_offset_top){
			$('#hidden_menu').css({ 'position': 'fixed', 'top':0, 'left':0, 'opacity': 1 });
			$('#emergency_number').addClass('top');
			$('#quiero_donar_btn_wrapper').addClass('top');
		}
		else {
			$('#hidden_menu').css({ 'position': 'fixed', 'top': 5000, 'opacity': 0});   	
			$('#emergency_number').removeClass('top');
			$('#quiero_donar_btn_wrapper').removeClass('top');
			}
		
	};
	sticky_navigation();
	$(window).scroll(function() {
		sticky_navigation();
	});	
}
function donations_stick()
{
	if($('#donations_menu').offset())
	var donations_offset_top = $('#donations_menu').offset().top;
	var sticky_donation = function(){
		var don_scroll_top = $(window).scrollTop();
		don_scroll_top+=68;
		if (don_scroll_top > donations_offset_top)
			$('#donations_menu').css({ 'position': 'fixed', 'top': 53, 'display':'block' });
		else 
			$('#donations_menu').css({ 'position': 'relative', 'top': 0, 'display':'block'});
			
		if (don_scroll_top > 2530)
			$('#donations_menu').css({ 'display':'none' });
	};
	sticky_donation();
	$(window).scroll(function() {
		sticky_donation();
	});
}

function ambulance_tools()
{
	$("#lista_el li").hover(function(){
		var currentId = $(this).attr('id');
		$('#lista_elementos li').removeClass('visible').addClass('');
		
		$('#lista_elementos #'+currentId+'_content').addClass('visible');
	

	});
		
}
function contact_map()
{
	$("#map_nav div").click(function(){
		var currentId = $(this).attr('id');
		$('#intro_contacto div').removeClass('visible').addClass('');
		
		$('#intro_contacto #map_'+currentId).addClass('visible');
	

	});
	
}

function load_logros()
{
	$('.slider_logros')	
		.cycle({ 
		    fx:     'fade', //slider_logros
		    delay:  -3000 ,
		    next:   '#logros_next', 
	    	prev:   '#logros_prev',
	    	pager:  '#logros_nav',
	    	after: function(currSlideElement, nextSlideElement, options, forwardFlag) {
	    		anchor = $(nextSlideElement).children()
	    		category = $(anchor).attr('alt')
	    		$('#logros_categoria').fadeIn().html(category)
	    	},
		})
}

function load_youtube_video()
{
	$('#video_wrapp').html('<iframe width="382" height="229" src="//www.youtube.com/embed/1GTgOozOTVY" frameborder="0" allowfullscreen></iframe>)');
}

function load_news()
{
	slides_no = $('.slider_news div').length;
	if(slides_no > 1)
	{
		$('.slider_news')	
		.cycle({ 
		    fx:     'scrollVert', 
		    delay:  -3000 ,
		    next:   '#news_next_2', 
	    	prev:   '#news_prev_2', 
	    	cleartypeNoBg: true   	
		});
	}
}

function load_vertical_slider()
{
	$('.slider_vert')	
	.cycle({ 
	    fx:     'scrollVert', 
	    next:   '#news_next', 
    	prev:   '#news_prev',
    	timeout: 15000,
	});
}

function load_vertical_horz()
{
	page = extras.get_currentpage()
	timeout = (page == 'ambulancias') ? 25 * 1000 : 1000;
		
	$('.slider_horz')	
	.cycle({ 
	    fx:     'scrollHorz', 
	    next:   '.slider_horz_next', 
    	prev:   '.slider_horz_prev', 
    	timeout: timeout,   	
	});	
}

function load_cycle_slider(effect)
{
	$('.slideshow').cycle({
		fx: effect
	})
}

function load_mint_sliders()
{
	$('.slider_nav a').click(function(){
		//extras.mint_slider(this)
		return false
	})
}

function load_campanas_fancybox()
{
	$("a[rel=fancybox_campanas]").fancybox({
		'transitionIn'		: 'none',
		'transitionOut'		: 'none',
		'titlePosition' 	: 'over',
		'titleFormat'       : function(title, currentArray, currentIndex, currentOpts) {
		    return '<span id="fancybox-title-over">Image ' +  (currentIndex + 1) + ' / ' + currentArray.length + ' ' + title + '</span>';
		}
	});
}

function get_last_tweets()
{
	$.post('get_last_tweets', function(data) {
		$('#twitter_panel').html(data);
		$('#twitter_panel').cycle({ 
		    fx:      'scrollDown', 
		    delay:   -3000,
		    cleartypeNoBg: true
		});
	});	
}

/*
function load_news_home(mouseEnteredSlider)
{
	setInterval(function() {
		if(!mouseEnteredSlider) {
			if($('.cbp-fwnext').css('display') != 'none'){
				$('.cbp-fwnext').click();
			} else {
				$('.cbp-fwdots span:first-child').click();
			}
		}
	}, 10000);
}
*/
