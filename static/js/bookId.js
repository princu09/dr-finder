$(document).ready(function() {
    $('#approveId').click(function(e) {
        valueGet = $('#bookId').val();
        $('#bookIdPut').val(valueGet);
    });
    $('#deniedId').click(function(e) {
        valueGet = $('#bookId').val();
        $('#bookIdPut2').val(valueGet);
    });
});