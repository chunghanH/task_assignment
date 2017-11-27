$('#task_form').submit(function() {
    var c = confirm("按好繼續?");
    return c;
});

$(function(){
    $('#datepicker').datepicker({
        dateFormat: 'yy-mm-dd'
    });
});
