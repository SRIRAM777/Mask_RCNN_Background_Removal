$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				image_url : $('#name-field').val()
			},
			type : 'POST',
			url : '/image_url'
		})
		.done(function(response) {

			
		});

		event.preventDefault();

	});

});