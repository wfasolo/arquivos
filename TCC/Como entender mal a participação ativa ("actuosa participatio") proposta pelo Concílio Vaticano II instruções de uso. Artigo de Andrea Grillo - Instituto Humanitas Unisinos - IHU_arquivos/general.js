
/**
 * Intercepta a response para a função de parsing.
 *
 * @author Marcelo Henrique <marcelohenrique180@asav.org.br>
 * 
 * @returns void
 */
function saveToStorage(user) {
  localStorage.setItem('userToken', user.accessToken);
  localStorage.setItem('userID', user.userID);
  localStorage.setItem('profilePic', user.profilePic);
  localStorage.setItem('name', user.name);
  localStorage.setItem('social', user.social);
}

function getUser() {
  var user = {
    userToken: localStorage.getItem('userToken'),
    userID: localStorage.getItem('userID'),
    profilePic: localStorage.getItem('profilePic'),
    name: localStorage.getItem('name'),
    social: localStorage.getItem('social')
  };

  return user;
}

function isLogged() {
  return localStorage.getItem('userID') !== null;
}

function logout(ui) {
  var social = getUser().social;

  switch (social) {
    case 'facebook':
      FB.logout();
      break;

    default:
      break;
  }

  localStorage.removeItem('userID');
  localStorage.removeItem('userToken');
  localStorage.removeItem('profilePic');
  localStorage.removeItem('social');
  localStorage.removeItem('name');

  refreshLogin(ui);
}

function refreshLogin(ui) {
  var user = getUser();
  ui.logoutButton.show();


  if (isLogged()) {
    ui.socialIcons.hide();
    ui.logoutButton.show();
    ui.pictureHolder.attr('src', user.profilePic);
  } else {
    ui.socialIcons.show();
    ui.logoutButton.hide();
    ui.pictureHolder.attr('src', ui.defaultPicture);
  }
}
