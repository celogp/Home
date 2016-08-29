var csrftoken = getCookie('csrftoken');

$(document).ready(function () {
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
	
	/* 
		botões de formulários
	$('#btnLogin').on('click', function() { onFazerLogin(); });
	*/
	$('#btnSalvarTitulo').on('click', function() { onSalvarForm($('#FrmTitulos')); });
	$('#btnPesTitulos').on('click', function() { onPesTitulos($('#btnPesTitulos')); });
});


function onSalvarForm(frm){
	console.log ('ponto 1');
			/*
			dessa forma faz validação
			*/
			frm.submit(function (e) {
					e.preventDefault();
					$.ajax({
							type: 'POST',
							url: window.location.href,
							data: frm.serialize(),
							cache: false,
							success: function (data) {
								console.log ('passou no suscesso')
								$( "#ajaxerrors" ).addClass( "hidden" );
							},
							error: function(data) {
								console.log ('passou na falha forçada');
								$( "#ajaxerrors" ).removeClass( "hidden" );
								$("#ajaxerrors").html(data.responseText);

							}
					});
					console.log('fim do ajax');
			});
			
	return false;
};

function onFazerLogin(){
	var usuarioLogin = $('#username').val(),
		usuarioSenha = $('#password').val();
		parLoginAction = 'login/',
		parLoginDados = JSON.stringify( { username: usuarioLogin, password: usuarioSenha } )
		
	console.log (usuarioLogin);
	console.log (usuarioSenha);
	console.log (csrftoken);
/*	
	$.ajax({
		url: parLoginAction,
		type: 'post',
		data: {acao:parLoginAction, dados:parLoginDados},
	success: function(jsonData) {
		console.log(jsonData);
		console.log(jsonData.dados.username);
		console.log(jsonData.dados.password);
		console.log(jsonData.acao.status);
		console.log(jsonData.acao.mensagem);
		if (jsonData.acao.status == 'true') {
			console.log('verdadeiro');
		}
		location.href="home/";
	},
	failure: function(data) { 
		$("#msgWarning")[0].innerHTML = 'não cadastrado';
		$(".alert-warning").fadeTo(0, 1);
		$(".alert-warning").fadeTo(2000, 0).slideUp(1000, function(){
			$(this).hide(); 
		});			
	}
	}); 
	*/
	var frm = $('#LoginForm');
	console.log(frm);
	frm.submit(function () {
			$.ajax({
					type: 'POST',
					url: parLoginAction,
					data: frm.serialize(),
					success: function (data) {
						console.log ('passou no suscesso')
					},
					error: function(data) {
							console.log ('passou no false')
					}
			});
			//return false;
	});
	
	return true;
};

function onPesTitulos(){
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
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};