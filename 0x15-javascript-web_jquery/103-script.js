$(document).ready(function() {
    function translateHello() {
        const languageCode = $('#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

        $.get(apiUrl, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translateHello);

    $('#language_code').keypress(function(event) {
        if (event.which == 13) {
            translateHello();
        }
    });
});
