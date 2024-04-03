$(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('green');
    } else {
      $('header').removeClass('green').addClass('red');
    }
  });
});
