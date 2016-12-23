function likes_post(id) {
    
    var iurl = "/post_likes/123/";
    iurl = iurl.replace('123', id);
    
    $.ajax({
        url : iurl, 
        
        datatype:"html",

        // handle a successful response
        success : function(data) {
            $('#refresh_post').html(data);

        },

        // handle a non-successful response
        error : function(data,xhr,errmsg,err) {
            alert ("not work"  + data);
        }
    
    });
    
}







var timerRef;

function doSomething() {
    $.ajax("/editing/", {
        success: function(data) {
            $("#refresh_post").html(data);
        },
    });
}


$(function() {
    clearInterval(timerRef);               
    timerRef = setInterval(doSomething, 4000);
});

