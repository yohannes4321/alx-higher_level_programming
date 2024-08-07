$(document).ready(function () {
  $('#add_item').click(function () {
    const va = $('<li>Item</li>');
    $('ul.my_list').append(va);
  });
});
