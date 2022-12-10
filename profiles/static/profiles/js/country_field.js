let countryIsSelected = $('#id_default_country').val();
if(!countryIsSelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {
    countryIsSelected = $(this).val();
    if(!countryIsSelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});