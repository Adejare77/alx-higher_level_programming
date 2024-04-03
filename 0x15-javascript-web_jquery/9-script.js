$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .done((data) => {
      $('DIV#hello').text(data.hello);
    });
});
