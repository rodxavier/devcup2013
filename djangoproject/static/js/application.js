App = {}

App.initialize = function() {
  App.initialize_login();
}

App.initialize_login = function() {
  var username = $('.login-box .username-field').val();
  var password = $('.login-box .password-field').val();

  $('.login-box .button').click(function(){
    alert('testing');
  });
}

(function(){
  App.initialize();
})(jQuery)
