App = {}

App.initialize = function() {
  App.initialize_login();
  App.initialize_registration_form();
  App.initialize_logout();
  App.initialize_create_deal_form();
  App.initialize_sidebar();
}

App.initialize_sidebar = function() {
  $('.create-deal-link').click(function() {
    window.location = '/create_deal/';
  });

  $('.view-dashboard-link').click(function() {
    window.location = '/dashboard/';
  });
}

App.initialize_create_deal_form = function() {
  $('.create-deal-button').click(function(){
    $('.create-deal-form').submit();
  });
}

App.initialize_registration_form = function() {
  $('.register-box .button').click(function() {
    $('.register-box .success-message').hide();
    $('.register-box .error-message').hide();

    var username = $('.register-box .username-field').val();
    var password = $('.register-box .password-field').val();
    var password_confirmation = $('.register-box .confirm-password-field').val();
    var email = $('.register-box .email-field').val();
    var mobile = $('.register-box .mobile-field').val();

    if (username.length == 0) return App.registration_error('Username is required.');
    if (password.length == 0) return App.registration_error('Password is required.');

    if (password != password_confirmation) {
      return App.registration_error('Passwords do not match.');
    }

    if (email.length == 0) return App.registration_error('Email is required.');

    if (mobile.length == 0) return App.registration_error('Mobile is required.');

    $('.register-box .error-message').hide();

    var post_data = {
      username: username,
      password: password,
      password_confirmation: password_confirmation,
      email: email,
      mobile: mobile
    };

    $.post('/register/', post_data, function(data) {
      if (data == 'true') {
        $('.register-box .success-message').show();

        setTimeout(function(){
          window.location = '/dashboard/';
        }, 1000);
      } else {
        App.registration_error(data);
      }
    });
  });
}

App.registration_error = function(text) {
  var $error = $('.register-box .error-message');
  $error.html(text);
  $error.show();

  return false;
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

App.initialize_logout = function() {
  $('.logout-button').click(function(){
    window.location = '/logout/';
  });
}

$(function(){
  App.initialize();
});
