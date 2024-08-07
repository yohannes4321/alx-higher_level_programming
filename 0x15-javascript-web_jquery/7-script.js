$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (data) {
      const val = data.name;
      $('#character').append(val);
    }
  )
    .fail(function () {
      console.error('error fetching data');
    });
  $('#character').append(val);
});
