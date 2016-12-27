var what_page = 2;

function likes_post(id) {
    
    var iurl = "/post_likes/123/";
    iurl = iurl.replace('123', id);
    
    $.ajax({
        url : iurl, 
        
        datatype:"html",

        // handle a successful response
        success : function(data) {
            $('#refresh_post'+id).html(data);

        },

        // handle a non-successful response
        error : function(data,xhr,errmsg,err) {
            alert ("not work"  + data);
        }
    
    });
    
}

function page(tem){
    what_page = tem;
}





var timerRef;

function doSomething() {
    $.ajax(window.location.href, {
        success: function(data) {
            $("#refresh_post").html(data);
        },
    });
}


$(function() {
    clearInterval(timerRef);               
    timerRef = setInterval(doSomething, 4000);
});

