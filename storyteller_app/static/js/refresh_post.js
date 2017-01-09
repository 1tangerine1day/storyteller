var timerRef;

function doSomething() {
    $.ajax(
        url:window.location.href, {
        success: function(data) {
            $("#refresh_post").html(data);
        },
    });
}



$(function() {
    clearInterval(timerRef);               
    timerRef = setInterval(doSomething, 4000);
});

