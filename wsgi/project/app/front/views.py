from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
#from django.template import RequestContext
from app.front.data import Data
from app.front.menu import Menu
from app.data.models import Data_DB, TransparenciaMenu
from app.donativos.models import Campana, Logros
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from twitter import *
from mezzanine.blog.models import *
from mezzanine.blog.views import *
from django.core.mail import EmailMultiAlternatives	

menu = Menu()
data = Data()
data_db = Data_DB

def home(request, lang=0, tag=''):	
	section_data = data.home(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	campanas = Campana.objects.all().order_by('-weight')
	tmp = Logros.objects.all().order_by('-weight')
	logros = get_logros_lang(tmp, lang)
	posts = BlogPost.objects.all().order_by('-publish_date')[:5]
	return render_to_response('sections/home.html', locals())

def about_us(request, lang=0, tag=''):	
	section_data = data.about_us(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)

	ua = request.META.get('HTTP_USER_AGENT', '').lower()

	is_mobile = True if 'mobile' in ua else False
	#return HttpResponse(ua)
	return render_to_response('sections/about_us.html', locals())

def hospital(request, lang=0, tag=''):	
	section_data = data.hospital(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/hospital.html', locals())

def ambulance(request, lang=0, tag=''):	
	section_data = data.ambulance(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/ambulance.html', locals())

def donations(request, lang=0, tag=''):	
	section_data = data.donations(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/donations.html', locals())

def transparency(request, lang=0, tag='servicios-comunidad'):
	tmp = data_db.objects.filter(section=1)
	section_data_db = get_correct_lang(tmp, lang)
	section_data = data.transparency(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	tmp = TransparenciaMenu.objects.all()
	sub_menu = get_correct_items(tmp, lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/transparency.html', locals())
	

def contact(request, lang=0, tag=''):	
	tmp = data_db.objects.filter(section=2)
	section_data_db = get_correct_lang(tmp, lang)
	section_data = data.contact(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/contact.html', locals())

def news(request, lang=0, tag=''):	
	section_data = data.news(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/blog.html', locals())

def training_center(request, lang=0, tag=''):
	tmp = data_db.objects.filter(section=3)
	section_data_db = get_correct_lang(tmp, lang)
	section_data = data.training_center(lang)
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/training_center.html', locals())

def preparate(request, lang=0, tag='incendios'):
	tmp = data_db.objects.filter(section=5)
	section_data_db = get_correct_lang(tmp, lang)
	section_data = data.preparate(lang)	
	gral_info = data.gral(lang)
	main_menu = menu.get_main_menu(section_data['gral_info']['section'], lang)
	footer_menu = menu.get_footer_menu(lang)
	return render_to_response('sections/preparate.html', locals())

def get_logros_lang(data, lang):
	response = []
	for row in data:		
		if lang == 0:
			response.append({
				'text': row.text_sp,
				'link': row.link_sp,
				'category': row.category,
				})
		else:
			response.append({
				'text': row.text_en,
				'link': row.link_en,
				'category': row.category,
				})
	return response

def get_correct_lang(data, lang):
	response = []
	for row in data:		
		if lang == 0:
			response.append(row.text_sp)
		else:
			response.append(row.text_en)
	return response

def get_correct_items(data, lang):
	response = []
	for row in data:		
		if lang == 0:
			response.append({
				'title': row.title_sp,
				'href': row.href_sp,
				'alt': row.alt,
				})
		else:
			response.append({
				'title': row.title_en,
				'href': row.href_en,
				'alt': row.alt,
				})
	return response

@csrf_exempt
def get_last_tweets(request):	
	OAUTH_TOKEN = '305292335-b71eMUTczxCR6SmZpqYJ7EGWvxNhVBDaWWR2OS8p'
	OAUTH_SECRET = 'xIrNwr3uTXaNNIgkFjUYW34lbfY0gzn2b00uUjfzNEc'
	CONSUMER_KEY = 'Wk1JNvuzxn5OLG1QFeCxSw'
	CONSUMER_SECRET = '9yNS97TG3XqjsBbpjXnbOOFB2o0mKSyzRvpnK8AjM'
	response = ''
	i = 1;
	t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
	tmp = t.statuses.user_timeline()
	for row in tmp:
		response += "<div><a href=\"https://twitter.com/CruzRojaTijuana/status/" + str(row['id']) + "\" title=\"Ver twitt\" target=\"_blank\">" + row['text'] + "</a>"
		response += "<br><br></div>"
		if i == 5: break
		i += 1
	return HttpResponse(response)

@csrf_exempt
def send_mail_form(request):
	c = {}
	c.update(csrf(request))
	if request.is_ajax():
		response = 'error'
		email_msg = ''
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		phone = request.POST.get('phone', '')
		asunto = request.POST.get('asunto', '')
		message = request.POST.get('message', '')
		if name == '' or email == '' or message == '':
			response = 'empty_data'
		else:
			email_msg = """
				Name: <b>""" + str(name)  + """</b><br/>
				Email: <b>""" + str(email)  + """</b><br />
				Phone: <b>""" + str(phone)  + """</b><br />
				Subject: <b>""" + str(asunto)  + """</b><br />
				Message: <b>""" + str(message)  + """</b><br />
			"""
			try:
				text_content = 'Message sent it from contact form'
				html_content = email_msg
				msg = EmailMultiAlternatives('CR Contact Form', text_content, email, ['info.mintitmedia@gmail.com','contacto@cruzrojatijuana.org.mx', 'comunicacion@cruzrojatijuana.org.mx'])
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				response = "success"
			except Exception, e:
				response = e
		return HttpResponse(response, c)
	else:
		return HttpResponse(status=400)

