var csrftoken = getCookie('csrftoken');

$(document).ready(function () {
	$.ajaxSetup({
			beforeSend: function(xhr, settings) {
					if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
							xhr.setRequestHeader("X-CSRFToken", csrftoken);
					}
			}
	});
	
	$('#btnLogin').on('click', function() { onFazerLogin(); });
});

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