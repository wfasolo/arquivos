/**
 * Renderiza comentários já 'parsed' na tela
 * 
 * @author Marcelo Henrique <marcelohenrique180@asav.org.br>
 * 
 * @param {array JQuery} ui
 * @param {array} comments
 */
function renderComments(ui, comments) {
  var repalceDataFilled = _.partial(repalceData, ui)

  var renderedComments = _.map(repalceDataFilled)(comments);

  ui.commentsContainer.html(renderedComments);
}

// Função Auxiliar de renderComments
function repalceData(ui, comment) {
  var pictureUrl = getUserPicture(ui, comment.social_id, comment.social_type);

  var repalceDataFilled = _.partial(repalceData, ui);

  var commentOwnerFilled = _.partial(commentOwner, comment);

  // Função verifica se o comentário está sob moderação e aplica devidas modificações ao template
  var isOcult = function (template) {
    return comment.aproval_state !== '1' ?
      _.flow(
        replaceField('##OCULT', 'comment-ocult'),
        replaceField('##NAME', comment.name + ' (Em Moderação)')
      )(template)
      :
      _.flow(
        replaceField('##OCULT', ''),
        replaceField('##NAME', comment.name)
      )(template)
  }

  var replaceDate = function (template) {
    return replaceField("Invalid Date", "")(
      replaceField("##DATE",
        new Date(comment.created)
          .toLocaleDateString("pt-br", {
            day: "numeric",
            month: "short",
            year: "numeric",
            hour: "numeric",
            minute: "numeric"
          })
      )(template)
    )
  }

  var replaceChilds = function (template) {
    return comment.childs.length === 0 ?
      replaceField('##CHILD', '<div class="comment_thread"></div>')(template)
      :
      replaceField('##CHILD', '<div class="comment_thread">'
        + _.map(repalceDataFilled)(comment.childs).join('')
        + '</div>')(template)
  }

  return _.flow(
    replaceField(/##COMMENT_ID/g, comment.id),
    replaceField('##COMMENT', comment.comment.replace(/\n/g, "<br />")),
    replaceField('##PICTURE', pictureUrl),
    replaceField('##SOCIAL_ID', comment.social_id),
    replaceDate,
    isOcult,
    replaceChilds,
    commentOwnerFilled
  )(ui.commentTemplate)
}

function commentOwner(comment, template) {
  if (!isLogged()) {
    return replaceField('##DELETE_DISPLAY', 'hide')(template);
  }

  var user = getUser();

  if (comment.social_id === user.userID && comment.social_type === user.social) {
    return replaceField('##DELETE_DISPLAY', '')(template);
  }

  return replaceField('##DELETE_DISPLAY', 'hide')(template);
}

function getUserPicture(ui, userId, socialMedia) {
  switch (socialMedia) {
    case 'facebook':
      return 'https://graph.facebook.com/' + userId + '/picture?width=300';

    default:
      return ui.defaultPicture;
  }
}

function replaceField(field, value) {
  return function(template) {
    return template.replace(field, value)
  }
}

/**
 * Adiciona caixa de novo comentário na tela depois do comentário selecionado
 * 
 * @author Marcelo Henrique <marcelohenrique180@asav.org.br>
 * 
 * @param {array JQuery} ui
 * @param {JQuery} commentNode
 * @param {int} commentId
 */
function addCommentBox(ui, commentNode, commentId) {

  var newComment =
    _.flow(
      replaceField('##COMMENT_ID', commentId),
      replaceField('##PICTURE', getUserPicture(ui, getUser().userID, getUser().social))
    )(ui.newCommentTemplate);

  var newCommentBox = commentNode.parent().parent().next();

  newCommentBox.prepend(newComment);

  return newCommentBox.children()[0];
}