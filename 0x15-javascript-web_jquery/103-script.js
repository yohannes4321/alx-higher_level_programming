$(document).ready(function () {
  function fetchTranslation () {
    // Get the language code from the input field
    const langCode = $('#language_code').val();

    // Fetch translation from the API
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: { lang: langCode },
      success: function (data) {
        // Display the translation in the div#hello
        $('#hello').text(data.hello);
      },
      error: function () {
        // Handle error if the API request fails
        $('#hello').text('Error fetching translation');
      }
    });
  }

  // Bind click event to the button
  $('#btn_translate').click(fetchTranslation);

  // Bind keypress event to the input field
  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // Check if Enter key is pressed
      fetchTranslation();
    }
  });
});
