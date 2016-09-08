$(document).ready(function () {
	var csrftoken = getCookie('csrftoken');

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$('.left.demo.sidebar').first()
		.sidebar('attach events', '.open.item', 'show')
		.sidebar('setting', 'transition', 'overlay')
	;

	$('.open.item')
		.removeClass('disabled')
	;

	$('.ui.search')
		.search({
			debug: false,
			apiSettings: {
			action:'search',
      url: '?filter_text={query}', 
			onResponse: function(Response) {
				console.log(Response)
			}
			},
			fields: {
				results : 'rows',
				title   : 'descricao'
			},
			cache: false,
			minCharacters : 3
		})
	;

	$('.message .close')
		.on('click', function() {
			$(this)
				.closest('.message')
				.transition('fade')
			;
		})
	;

	$('.dropdown')
		.dropdown({
			transition: 'drop'
		})
	;
	
	$('.ui.accordion')
		.accordion()
	;
	
	/* 
		botões de formulários
	*/
	$('#FazerLogin').on('click', function() { onSubmitFormLogin($('#FrmLogin')); });
	
	$('#SalvarTitulo').on('click', function() { onSubmitForm($('#FrmTitulos'), 'POST'); });
	$('#ApagarTitulo').on('click', function() { onSubmitForm($('#FrmTitulos'), 'DELETE'); });
	$('#PesquisarTitulos').on('click', function() { onPesTitulos($('#PesquisarTitulos')); });
	
});

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
					}
			}
	}
  return cookieValue;
};

function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

function setMsg(msg, opc) {
	if (opc == 'success') {
		$("#ajaxmsgsucesso").removeClass( 'hidden' );
		$('#ajaxsucesso').html(msg);
		setTimeout( function() {
			$("#ajaxmsgsucesso").addClass( 'hidden' );	
			$('#ajaxsucesso').html();
			
		}
		, 1000);
	} else if (opc == 'danger') {
		$("#ajaxmsgerro").removeClass( 'hidden' );
		$('#ajaxerrors').html(msg);
		setTimeout( function() {
			$("#ajaxmsgerro").addClass( 'hidden' );	
			$('#ajaxmsgerro').html();
		}
		, 3000);
	}
	return false;
};

function onSubmitForm(frm, verbo){
	if (verbo == null || verbo == undefined){
		verbo = 'POST';
	}
	$.ajax({
			type: verbo,
			url: window.location.href,
			data: frm.serialize(),
			cache: false,
			success: function (data) {
				if (verbo == 'DELETE') {
					setMsg('Registro apagado com sucesso.', 'success');
				}else{
					setMsg('Registro salvo com sucesso.', 'success');
				}
			},
			error: function(data) {
				setMsg(data.responseText, 'danger');
				window.location;
			}
		});
	return false;
};

function onSubmitFormLogin(frm){
	$.ajax({
			type: 'POST',
			url: 'login/',
			data: frm.serialize(),
			cache: false,
			success: function (data) {
				window.location = '/home/';
			},
			error: function(data) {
				setMsg(data.responseText, 'danger');
				window.location;
			}
		});
	return false;
};

function onPesTitulos(){
	var txtConteudo = $('#txtConteudo').val(),
			parDados = '?filter_text=' + txtConteudo;
	$.ajax({
		type: 'POST',
		url: window.location.href+parDados,
		success: function (data) {
			$('#results').html(data);
		},
		error: function(data) {
			console.log ('passou no false')
		}
	});
	return true;
};

/*
	para pegar retorno json,pequisa intra telas
function onPesTitulosOld(){
	var txtTitulo = $('#txtTitulo').val(),
		parAction = 'pestitulos/',
		parDados = '?filter_text=' + txtTitulo
		
	console.log(parDados);
	$.ajax({
			type: 'POST',
			url: parAction+parDados,
			data: parDados,
			success: function (data) {
				console.log ('passou no suscesso')
				console.log (data)
				$('#lisTitulos').html(data);
				
			},
			error: function(data) {
					console.log ('passou no false')
			}
	});
	return true;
};
*/