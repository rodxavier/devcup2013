App = {}

App.initialize = function() {
  App.initialize_login();
}

App.initialize_login = function() {
  $('.login-box .button').click(function(){
    var username = $('.login-box .username-field').val();
    var password = $('.login-box .password-field').val();

    $.post('/login/', {'username': username, 'password': password}, function(data){
      if (data == 'true') {
        $('.login-box .error-message').hide();
        $('.login-box .success-message').show();

        setTimeout(function(){
          window.location = '/dashboard/';
        }, 1000);
      } else {
        $('.login-box .error-message').show();
      }
    });
  });
}

$(function(){
  App.initialize();
});
