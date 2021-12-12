//signup and login form
$(document).ready(function(){
    $(".login-form").hide();
    $(".login").css("background", "#F7F7F7");
    $(".login").click(function(){
      $(".signup-form").hide();
      $(".login-form").show();
      $(".signup").css("background", "#F7F7F7");
      $(".login").css("background", "#fff");
    });
    $(".signup").click(function(){
      $(".signup-form").show();
      $(".login-form").hide();
      $(".login").css("background", "#F7F7F7");
      $(".signup").css("background", "#fff");
    });
  });
//validation signup
$(document).ready(function(){
    // Validate Username
    $('#firstname_check').hide();   
    $('#first_name').keyup(function () {
        validateUsername();
    });
     
    function validateUsername() {
      let usernameValue = $('#first_name').val();
      if (usernameValue.length==0) {
        $('#firstname_check').show();
        $('#firstname_check').html("**Name must not be empty");
        return false;
      }
      else if(usernameValue.length < 3){
          $('#firstname_check').show();
          $('#firstname_check').html("**Length of username must be more than 2");
          return false;
      }
      else {
          $('#firstname_check').hide();
          return true;
      }
    }
 
    // Validate Email
    $('#emailcheck').hide();
    $('#email').keyup(function () {
      validateEmail();
    });
    function validateEmail(){
      let EmailValue=$('#email').val();
      let regex=/^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
      if(regex.test(EmailValue)){
        $('#emailcheck').hide();
        return true;
      }
      else{
        $('#emailcheck').show();
        $('#emailcheck').html("Your email must be a valid email");
        return false;
      }
    }
     
   // Validate Password
    $('#passcheck').hide();
    $('#password').keyup(function () {
        validatePassword();
    });
    function validatePassword() {
        let passwrdValue =$('#password').val();
        if (passwrdValue.length == 0) {
            $('#passcheck').show();
            $('#passcheck').html("**Password must not be empty");
            return false;
        }
        else if (passwrdValue.length < 5) {
            $('#passcheck').show();
            $('#passcheck').html("**Length of your password must be more than 5");
            return false;
        } 
        else {
            $('#passcheck').hide();
            return true;
        }
    }
         
    // Validate Confirm Password
    $('#conpasscheck').hide();
    $('#conpassword').keyup(function () {
        validateConfirmPasswrd();
    });
    function validateConfirmPasswrd() {
        let confirmPasswordValue =$('#conpassword').val();
        let passwrdValue =$('#password').val();
        if (passwrdValue != confirmPasswordValue) {
            $('#conpasscheck').show();
            $('#conpasscheck').html("**Password didn't Match");
            return false;
        } else {
            $('#conpasscheck').hide();
            return true;
        }
    }
     
    // signup button
    $('#signup_btn').click(function () {
      if(validateUsername()&&validatePassword()&&validateConfirmPasswrd()&&validateEmail()){
        return true;
      }
      else{
        return false;
      }
    });
});
//validation login
$(document).ready(function(){
    // Validate signin Email
    $('#log_emailcheck').hide();
    $('#log_email').keyup(function () {
      validatelogEmail();
    });
    function validatelogEmail(){
      let logEmailValue=$('#log_email').val();
      let regex=/^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
      if(regex.test(logEmailValue)){
        $('#log_emailcheck').hide();
        return true;
      }
      else{
        $('#log_emailcheck').show();
        $('#log_emailcheck').html("Your email must be a valid email");
        return false;
      }
    }
    
    // Validate Password
    $('#log_passcheck').hide();
    $('#log_password').keyup(function () {
        validatelogPassword();
    });
    function validatelogPassword() {
        let passwordValue =$('#log_password').val();
        if (passwordValue.length == 0) {
            $('#log_passcheck').show();
            $('#log_passcheck').html("**password must not be empty");
            return false;
        }
        else if (passwordValue.length < 5) {
            $('#log_passcheck').show();
            $('#log_passcheck').html("**length of your password must be more than 5");
            return false;
        } 
        else {
            $('#log_passcheck').hide();
            return true;
        }
    }

    // Submit button
    $('#login_btn').click(function () {
      if(validatelogPassword()&&validatelogEmail()){
        return true;
      }
      else{
        return false;
      }
    }); 
});

//flash_message
$(document).ready(function(){
  $("#flash_message").click(function(){
    var div = document.getElementById('flash_container');
    div.parentNode.removeChild(div);
  });
});
//for searching
$(document).ready(function(){
  $("#Searching").on("keyup change clear", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr #task").filter(function() {
      return $(this).text().indexOf(value) == -1;
    }).parent().hide();
    $("#myTable tr #task").filter(function() {
      return $(this).text().indexOf(value) !== -1;
    }).parent().show();
  });
});
