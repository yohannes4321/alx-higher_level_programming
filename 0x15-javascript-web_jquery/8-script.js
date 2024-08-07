$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    for (const film of data.results) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    }
  }).fail(function () {
    console.error('error');
  });
});
