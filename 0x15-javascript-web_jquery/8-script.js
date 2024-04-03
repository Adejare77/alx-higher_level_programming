$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const moviesList = data.results;
  $.each(moviesList, function (index, element) {
    $('UL#list_movies').append(`<li>${element.title}</li>`);
  });
});
