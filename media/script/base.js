jQuery(function(){
	jQuery(document).ready(function() {
		
		// Beautify ampersands.
	    jQuery("*:contains('&')", document.body)
	        .contents()
	        .each(
	            function() {
	                if( this.nodeType == 3 ) {
	                    jQuery(this)
	                        .replaceWith( this
	                            .nodeValue
	                            .replace( /&/g, '<span class="ampersand">&</span>')
	                        );
	                }
	            }
	        );
	});
});