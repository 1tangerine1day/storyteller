function likes_post(id) {
    
    var iurl = "/post_likes/123/";
    iurl = iurl.replace('123', id);
    
    var idiv = "#refresh_like_123";
    idiv = idiv.replace('123', id);
    
    
    $.ajax({
        url : iurl, 
        
        datatype:"html",

        // handle a successful response
        success : function(data) {
            $(idiv).html(data);

        },

        // handle a non-successful response
        error : function(data,xhr,errmsg,err) {
            alert ("not work"  + data);
        }
    
    });
    
}




function new() {
    
    $.ajax({
        url : "/new/", 
        
        datatype:"html",

        // handle a successful response
        success : function(data) {
            alert ("work"  + data);
            $(#refresh_post).html(data);

        },

        // handle a non-successful response
        error : function(data,xhr,errmsg,err) {
            alert ("not work"  + data);
        }
    
    });
    
}

function hot() {
    
    $.ajax({
        url : "/hot/", 
        
        datatype:"html",

        // handle a successful response
        success : function(data) {
            alert ("work"  + data);
            $(#refresh_post).html(data);

        },

        // handle a non-successful response
        error : function(data,xhr,errmsg,err) {
            alert ("not work"  + data);
        }
    
    });
    
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

