jQuery(document).ready(function(){

	//INSTITUCIONAL

	player = jQuery('.playerIframe');
	playerTitle = jQuery('.video > h4');

	jQuery('.thumbnailLink').click(function(event) {
		event.preventDefault();

		player.attr("src", this.href + "?autoplay=1");
		player.attr("title", this.title);
		player.attr("alt", this.alt);
		playerTitle.html(this.title);

		jQuery('.videoTitle').text(this.title);

	});



	//MODAL

	//Click on close button
	jQuery('.modal-close-button').click(function() {

		var parent = jQuery(this).parent();

		if(parent.is(':visible')) {

			console.log(parent.is(':visible'));

			parent.fadeToggle();
			parent.find('iframe').remove();
			jQuery("body").removeClass("body-overlayed");
		}

		return false;
	});

	jQuery('.activeModal').click(function() {

		jQuery(".modal-overlay").fadeToggle();
		jQuery("body").addClass("body-overlayed");

		var modalType 	= jQuery(this).attr('data-modal');

		if(modalType == 'video') {
			var videoUrl 	= jQuery(this).attr('data-src');
			var videoTitle 	= jQuery(this).attr('data-title');
			var iframe 		= '<iframe width="100%" src="' + videoUrl + '" frameborder="0" allowfullscreen>';
		}

		jQuery('.modal-content').html(iframe);
	});

});
