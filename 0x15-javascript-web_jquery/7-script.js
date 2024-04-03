$(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .done(function (response) {
      const characterName = response.name;
      $('DIV#character').text(characterName);
    });
});
