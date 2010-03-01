jQuery(function() {
	// setup ul.tabs to work as tabs for each div directly under div.panes
	jQuery("div#feature-list ul.tabs").tabs("div.panes > div.pane-content",
	                                        {
	                                            event: 'click',
	                                            effect: 'fade'
	                                        });
});
