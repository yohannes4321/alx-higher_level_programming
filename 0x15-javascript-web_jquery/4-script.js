$(document).ready(function () {
  $('#toggle_header').click(function () {
    const head = $('header');
    if (head.hasClass('red')) {
      head.removeClass('red').addClass('green');
    } else {
      head.removeClass('green').addClass('red');
    }
  });
});
