
/**
 * Inicializa SDK do Facebook
 *
 * @author Marcelo Henrique <marcelohenrique180@asav.org.br>
 * 
 * @returns void
 */
function initFacebook(ui){
  window.fbAsyncInit = function() {
    FB.init({
      appId            : '154074558361498',
      autoLogAppEvents : true,
      xfbml            : true,
      version          : 'v2.11'
    });
    FB.AppEvents.logPageView();

    var user = getUser();
    if (isLogged()) {
      if (user.social === 'facebook') {
        FB.api('/me?access_token=' + user.userToken, {fields: 'name'}, function(response) {
          if (!response || response.error) {
            logout(ui);
          }
        });
      }
    }
  };

  (function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
}


/**
 * Realiza login com Facebook, definindo variaveis locais
 *
 * @author Marcelo Henrique <marcelohenrique180@asav.org.br>
 * 
 * @param JQuery pictureHolder
 * @returns void
 */
function loginFacebook(ui) {
  FB.login(function(response) {
    if (response.authResponse) {
      
      var user = {
        userID: response.authResponse.userID,
        accessToken: response.authResponse.accessToken,
        social: 'facebook'
      };

      FB.api('/me', {fields: 'name'}, function(response) {

        user.name = response.name;
        user.profilePic = 'https://graph.facebook.com/'+user.userID+'/picture?width=300';
        
        saveToStorage(user);
        refreshLogin(ui);
        ui.socialIcons.hide();
      });
    }
  });
}
