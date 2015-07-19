$(function(){
	//location picking
	$("a#pick").click(function(){
		$(this).parent().children("div.pick.msg").html('Now click on the map to mark your location!');
		sessionStorage.pick = true;
	});

	var regex;
	$("#register").click(function(){
		//global vars
		var user = $("#register-form .username").val();
		var pass = $("#register-form .password").val();
		var confirm = $("#register-form .confirm").val();
		var email = $("#register-form .email").val();

		$.ajax({
		   url: "http://localhost:8000/api/v1/user/",
		   type: "POST",
		   contentType: "application/json",
			dataType:'json',
		   data: JSON.stringify({
				'type': 'register',
				'username': user,
				'email': email,
				'password1': pass,
				'password2': confirm
			}),
			success: function (msg) {
				console.log(msg)
			}, 
			error: function (msg) {
				console.log(msg)
			}
		});
		
	/*
		//empty error messages
		$("#register-form .errormsg").empty();

		regex = /\+\d{10}\b/;
		//firstname
		if($("#register-form .firstname").val() == "" || regex.test()){
			$("#register-form .username").addClass('error');
			$("#register-form .errormsg").append("Please enter a valid Firstname<br>");
		} else {
			$("#register-form .firstname").removeClass('error');
		}

		//lastname
		if($("#register-form .lastname").val() == ""){
			$("#register-form .lastname").addClass('error');
			$("#register-form .errormsg").append("Please enter a valid Lastname<br>");
		} else {
			$("#register-form .username").removeClass('error');
		}

		//username
		if($("#register-form .username").val() == ""){
			$("#register-form .username").addClass('error');
			$("#register-form .errormsg").append("Please enter a valid Username<br>");
		} else {
			$("#register-form .username").removeClass('error');
		}
		
		//password
		if($("#register-form .password").val() == ""){
			$("#register-form .password").addClass('error');
			$("#register-form .errormsg").append("Please enter a valid Password<br>");
		} else {
			$("#register-form .password").removeClass('error');
		}

		//confirm password
		if($("#register-form .password").val() == $("#register-form .confirm").val()){
			$("#register-form .password").addClass('error');
			$("#register-form .confirm").addClass('error');
			$("#register-form .errormsg").append("Passwords do not match<br>");
		} else {
			$("#register-form .password").removeClass('error');
			$("#register-form .confirm").removeClass('error');
		}
		
		regex = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
		//email
		if($("#register-form .email").val() == "" || !regex.test($("#register-form .email").val())){
			$("#register-form .email").addClass('error');
			$("#register-form .errormsg").append("Please enter a valid email<br>");
		} else {
			$("#register-form .email").removeClass('error');
		}

		
		//area of study
		console.log($("#register-form .area").val()[0] != $("#register-form .area").val()[0].toUpperCase());
		if($("#register-form .area").val() == "" || !$("#register-form .area").val()[0] == $("#register-form .area").val()[0].toUpperCase()){
			$("#register-form .area").addClass('error');
			$("#register-form .errormsg").append("Please enter your area of study<br>");
		} else {
			$("#register-form .area").removeClass('error');
		}
		
		regex = /\+\d{10}\b/;
		//number
		if(!regex.test($("#register-form .number"))){
			$("#register-form .number").addClass('error');
			$("#register-form .errormsg").append("Please enter a valid number<br>");
		} else {
			$("#register-form .number").removeClass('error');
		}

		//degree of study
		if($("#register-form .degree").val() == 'none'){
			$("#register-form .degree").addClass('error');
			$("#register-form .errormsg").append("Please select your degree<br>");
		} else {
			$("#register-form .degree").removeClass('error');
		}
		
	*/

	});

	$("#login").click(function(){
	var signinuser = $("#login-form .username").val();
	var signinpass = $("#login-form .password").val();
	
	$.ajax({
		url: "http://localhost:8000/api/v1/user/",
		type: "POST",
		contentType: "application/json",
		dataType:'json',
		data: JSON.stringify({
			'type': 'login',
			'username': signinuser,
			'password': signinpass
		}),
		success: function (msg) {
			//save to html5 session storage
			sessionStorage.session = msg;
			console.log(sessionStorage.session);
		}, 
		error: function (msg) {
			console.log(msg);
		}
	});

		/*
		//empty error messages
		$("#login-form .errormsg").empty();
		
		//username
		if($("#login-form .username").val() == ""){
			$("#login-form .username").addClass('error');
			$("#login-form .errormsg").append("Please enter a valid Username<br>");
		} else {
			$("#login-form .username").removeClass('error');
		}
		
		//password
		if($("#login-form .password").val() == ""){
			$("#login-form .password").addClass('error');
			$("#login-form .errormsg").append("Please enter a valid Password<br>");
		} else {
			$("#login-form .password").removeClass('error');
		}
		*/
	});
});
