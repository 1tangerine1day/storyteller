var timerRef;

function doSomething() {
    var iurl = window.location.href;
    $.ajax(iurl, {
        success: function(data) {
            alert ("work"  + data);
            $("#refresh_post").html(data);
        },
    });
}



$(function() {
    clearInterval(timerRef);               
    timerRef = setInterval(doSomething, 3000);
});