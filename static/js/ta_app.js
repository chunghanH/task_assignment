$('#task_form').submit(function() {
    var c = confirm("按好繼續?");
    return c;
});

$(function(){
    $('#datepicker1').datepicker({
        dateFormat: 'yy-mm-dd'
    });
});
