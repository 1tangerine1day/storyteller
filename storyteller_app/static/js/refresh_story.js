
 
var timerRef;

function doSomething() {
    var iurl = window.location.href;
    
        $.ajax(iurl, {
            success: function(data) {
                $("#refresh_story").html(data);
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
            $('#refresh_story').html(data);

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
            $('#refresh_story').html(data);

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
                $("#refresh_story").html(data);
                document.getElementById("context").value = "";
            },
            error: function(data) {
                $("#refresh_story").html("<h1>You did not login yet.</h1>");
            }
        });
        return false;
    });