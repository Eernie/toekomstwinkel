$(function() {
 $.get('/cart/', function(data) {
    $('#cart').html(data);
  });  
  setInterval(function(){
    $.get('/cart/', function(data) {
      $('#cart').html(data);
    });  
  },5000);
});