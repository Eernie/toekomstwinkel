$(function() {
  updatecart();
  setInterval(function(){
    updatecart();
  },1000);

  $(".add").click(function(){
    id = $(this).attr('id');
    $.get('/cart/'+id);
  });

});

function updatecart(){
    $.get('/cart/', function(data) {
      $('#cart').html(data);
    }); 
  };