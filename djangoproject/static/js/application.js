App = {}

App.initialize = function() {
  App.initialize_login();
}

App.initialize_login = function() {
  $('.login-box .button').click(function(){
    var username = $('.login-box .username-field').val();
    var password = $('.login-box .password-field').val();

    $.post('/login/', {'username': username, 'password': password}, function(data){
      alert(data);
    });
  });
}

$(function(){
  App.initialize();
});
