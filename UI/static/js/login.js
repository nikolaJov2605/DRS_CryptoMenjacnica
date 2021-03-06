$(document).ready(function(){
	$("#log_form").validate();
	
	$('#log_form input').on('keyup blur', function () { // fires on every keyup & blur
        if ($('#log_form').valid()) {                // checks form for validity
            $('#login').prop('disabled', false);        // enables button
        } else {
            $('#login').prop('disabled', 'disabled');   // disables button
        }
    });
	$('#id_error').hide();
	$('#id_errori').hide();
	
});

$(document).ready(function(){
	$('#login').click(function(){
		event.preventDefault();
		$.ajax({
			url: endpoint + '/logIn',
			data: $('#log_form').serialize(),
			type: 'POST',
			success: function(response){
				document.cookie = "username=" + response["cookie"]
				window.location.href = response["redirect"]
			},
			error: function(error){
				console.log(error)
				window.location.href = "/logIn"
			}
		});
	});
});
