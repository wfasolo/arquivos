/**
 * Faz requisição ao servidor por comentários públicos.
 * 
 * @param {JQuery} allCommentsForm
 * @returns Promise
 */
function fetchComments(allCommentsForm) {
  var destiny = allCommentsForm.attr('action');

  var data = allCommentsForm.serialize();

  if (isLogged()) {
    data += "&userToken=" + getUser().userToken;
    data += "&social=" + getUser().social;
  }

  return jQuery.ajax({
    url: destiny,
    data: data,
    dataType: 'json'
  });
}

/**
 * Envia novo comentário ao servidor.
 * 
 * @param {JQuery} allCommentsForm
 * @returns Promise
 */
function sendComment(newCommentForm) {
  var destiny = newCommentForm.attr('action');

  var userToken = 'userToken=' + localStorage.getItem('userToken');
  var social = 'social=' + localStorage.getItem('social');

  var formData = newCommentForm.serialize();

  var data = [
    formData,
    userToken,
    social
  ].join('&')

  return jQuery.ajax({
    url: destiny,
    method: 'post',
    data: data,
    dataType: 'json'
  });
}

/**
 * Remove comentário pela Api.
 * 
 * @param {JQuery} allCommentsForm
 * @returns Promise
 */
function deleteComment(deleteCommentForm, commentId) {
  var userToken = getUser().userToken;

  var destiny = deleteCommentForm.attr('action');

  var userToken = 'userToken=' + localStorage.getItem('userToken');
  var social = 'social=' + localStorage.getItem('social');
  commentId = 'comment_id=' + commentId;

  var formData = deleteCommentForm.serialize();

  var data = [
    commentId,
    formData,
    userToken,
    social
  ].join('&')

  return jQuery.ajax({
    url: destiny,
    method: 'post',
    data: data,
    dataType: 'json'
  });
}
