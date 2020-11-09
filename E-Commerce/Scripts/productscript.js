//Air max Product page product transition function 

$(document).ready(function() {

  $('.color-choose input').on('click', function() {
      var shoeColor = $(this).attr('data-image');

      $('.active').removeClass('active');
      $('.left-column img[data-image = ' + shoeColor + ']').addClass('active');
      $(this).addClass('active');
  });

});
