$(document).ready(function(){
	$('#logOut').click(function(){
		document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
		document.location.href = '/logIn'
	});
});