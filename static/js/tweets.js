"use strict";

// Generate new tweet using same screen name
$( "#tweet-btn" ).click( function() {
	$.get( "/new-tweet" ) 
		.done( function( result ) {
			$( "#tweet-text" ).html( result );
			console.log( "You clicked the button!" );
		});
});

// Get all the saved tweets 
$( "#saved-tweets" ).click( function() {
	$.get( "/view-tweets", function( result ) {
		$( "#view-tweets" ).html( result );
	}); 
});




