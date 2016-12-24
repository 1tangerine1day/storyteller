
var mode = 1;
var timerRef;

function doSomething() {
    var iurl = window.location.href;
    
        $.ajax(iurl, {
            success: function(data) {
                $("#card").html(data);
                if (mode==0){
                    document.getElementById("front").style.visibility='hidden';
                }
            },
        });
}


$(function() {
    clearInterval(timerRef);
    timerRef = setInterval(doSomething, 4000);
});


function likes_story(id) {
    
    var iurl = "/likes/123/";
    iurl = iurl.replace('123', id);
    
    $.ajax({
        url : iurl, 
        
        datatype:"html",

        // handle a successful response
        success : function(data) {
            $('#card').html(data);

        },

        // handle a non-successful response
        error : function(data,xhr,errmsg,err) {
            alert ("not work"  + data);
        }
    
    });
    
}

function likes_in_post(id) {
    
    var iurl = "/in_post_likes/123/";
    iurl = iurl.replace('123', id);
    
    $.ajax({
        url : iurl, 
        
        datatype:"html",

        // handle a successful response
        success : function(data) {
            $('#refresh_bottom').html(data);

        },

        // handle a non-successful response
        error : function(data,xhr,errmsg,err) {
            alert ("not work"  + data);
        }
    
    });
    
}

var frm = $('#add_story_form');
    frm.submit(function () {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                $("#card").html(data);
                document.getElementById("context").value = "";
            },
            error: function(data) {
                $("#card").html("<h1>You did not login yet.</h1>");
            }
        });
        return false;
    });
    

function flip_dialog(message, html) {	
    
	$('.flip-container').addClass('hover');
	mode = 0;
	document.getElementById("front").style.visibility='hidden';

	$("#comment").hide(1500);
	$(".end-line").hide(2000);
	
  	
}


function flip_dialog2(message, html) {
	
	$('.flip-container').removeClass('hover');
	mode = 1;
	document.getElementById("front").style.visibility='visible';
	
	$("#comment").show(1500);
	$(".end-line").show(2000);

	
}
 
    