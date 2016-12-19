/**
 * @author http://blazeboy.me
 */

function flip_dialog(message, html) {	
    
	$('.flip-container').addClass('hover');

	$("#comment").hide(1500);
	$(".end-line").hide(2000);
	document.getElementById("front").style.visibility='hidden';
  	
}


function flip_dialog2(message, html) {
	
	$('.flip-container').removeClass('hover');
	
	$("#comment").show(1500);
	$(".end-line").show(2000);
	document.getElementById("front").style.visibility='visible';
	
}


$(function() {
	
	$('#flipper-view').click(function() {
		flip_dialog("");
	});
	
	$('#flipper-edit').click(function() {
		flip_dialog2("");
	});

});

