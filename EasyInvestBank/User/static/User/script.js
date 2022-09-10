
$(document).ready (function(){
    $("#success-alert").hide();
    $("myAlert").click(function showAlert() {
        $("#success-alert").alert();
        window.setTimeout(function () {
            $("#success-alert").alert('close');
        }, 2000);
    });
});