/* developed by mintitmedia.com */

var extras = {

/**************** LOGIN ****************/
	//position:0,1		vertical, horizontal
	mint_slider: function (obj){
		
		dir = $(obj).attr('href')
		sign = (dir == 'next') ? '-':'+'
		parent = $(obj).parent().next()
		howmany_children = parent.children().length
		size = $(parent).attr('data-height')
		position = $(parent).attr('data-position')

		limit = (howmany_children-1) * size * -1
		
		margin_zero = $(parent).css('top').replace('px', '')
		margin_zero = isNaN(margin_zero) ? 0 : margin_zero

		can_prev = margin_zero < 0 ? true : false
		can_next = margin_zero > limit ? true : false

		/*
		console.log(parent)
		console.log('dir: '+ dir)
		console.log('howmany_children: '+ howmany_children)
		console.log('size: '+ size)
		console.log('position: ' + position)
		console.log('limit: ' + limit)
		console.log('margin_zero: ' + margin_zero)
		console.log('can_prev: '+ can_prev)
		console.log('can_next: '+ can_next)
		*/
		
		if( (dir == 'next' && can_next) || (dir == 'prev' && can_prev) )
			if(position == 'vertical')
				$(parent).animate({top:sign+"="+size+"px"},500);
	},

	get_currentpage: function (){
		var loc = window.location;
		p = loc.href.substring(loc.href.indexOf(loc.host) + loc.host.length + folder.length );
		if(p == '') p = 'inicio';
		return p;
	},



	gotoTop: function(id){
		if(id.length)
			$('html, body').animate({
				scrollTop: $('#'+id).offset().top + -50
			}, 1250);
	},

	isValidEmailAddress: function(emailAddress) {
	    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
	    return pattern.test(emailAddress);
	},

	getFirstItem: function(cadena){
	       var params = cadena.split('/');
	       return params[0];
	},

	getLastItem: function(cadena){
	       var params = cadena.split('/');
	       return params.pop();
	},

	get_server_path: function(){
		var loc = window.location;
		return "http://" + loc.hostname;
	},

	turon_page: function(tag)
	{
		$('#'+tag).animate({
			'opacity': '1',
			}, 'slow'
		)
		$('#wrapper').find('.animated').animate({
			'opacity': '1',
			}, 'slow'
		)

	},

	update_path: function(tag)
	{
		window.history.pushState(tag, tag, tag);
	},
}

//var obj_ucash = new Ucash();