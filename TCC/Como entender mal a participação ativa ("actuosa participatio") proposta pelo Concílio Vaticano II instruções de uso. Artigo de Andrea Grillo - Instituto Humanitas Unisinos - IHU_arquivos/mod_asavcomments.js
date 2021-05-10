(function ($) {

  $(document).ready(function () {

    /* Inicializar varáveis */
    var newCommentForm = $('form[name="new_comment"]');
    var allCommentsForm = $('form[name="comments"]');
    var deleteCommentForm = $('form[name="delete_comment"]');
    var commentTemplate = $('#comment_template').html();
    var newCommentTemplate = $('#new_comment_template').html();
    var commentsContainer = $('#comments');
    var facebookLoginButton = $('#facebook_login');
    var pictureHolder = $('form[name="new_comment"] .commentator_pic');
    var defaultPicture = $('#default_picture').attr('data-service');
    var logoutButton = $('#logout');
    var socialIcons = $('#new_comment_social')

    // Variável de estado para caixa de resposta de comentário
    var replyComment;

    /* Isola interações com o DOM a partir do objeto 'ui' */
    var ui = {
      commentTemplate: commentTemplate,
      commentsContainer: commentsContainer,
      pictureHolder: pictureHolder,
      defaultPicture: defaultPicture,
      logoutButton: logoutButton,
      newCommentTemplate: newCommentTemplate,
      socialIcons: socialIcons,
      refreshUI: startup // Função que recarrega dados na tela
    };

    /* Inicializa Redes Socias */
    initFacebook(ui);

    /* ====== STARTUP da Aplicação ====== */
    function startup() {
      parseCommentsFromRequest(fetchComments(allCommentsForm))
        .then(function (comments) {
          // console.log(comments)

          renderComments(ui, comments)
        })
    }

    refreshLogin(ui);
    startup();
    /* ====== STARTUP da Aplicação ====== */

    // Event Handlers

    facebookLoginButton.on('click', function (e) {
      e.preventDefault();
      loginFacebook(ui); // assíncrono, logo ui vai mudar depois de chamar api
    })

    logoutButton.on('click', function (e) {
      e.preventDefault();

      logout(ui);
      ui.refreshUI();
    })

    $(document).on('click', '.refresh_comments', function (e) {
      e.preventDefault();
      ui.refreshUI();
      var refresh = $($(e.currentTarget)[0].children[0].children[0]);
      refresh.addClass("refresh_comments-animate");
      setTimeout(function () {
        refresh.removeClass("refresh_comments-animate");
      }, 1000)
    });

    // Lidar com Submit de novo comentário
    $(document).on('submit', 'form[name="new_comment"]', function (e) {
      e.preventDefault();
      var comment = $(e.currentTarget);
      var commentButton = $(comment.find('#new_comment_submit')[0]);
      var textareaComment = $(comment.find('#textarea_comment')[0]);
      var alertBox = $($(commentButton).parent().children()[0]);

      if (isLogged()) {
        /*
        commentButton.addClass('new_comment_submitted');

        setTimeout(function () {
          commentButton.removeClass('new_comment_submitted')
        }, 1000);
        */

        var user = getUser();

        if (user.userToken) {
          sendComment(comment)
            .done(function (message) {
              dialogAlert(alertBox, 'Comentário Enviado', "success");

              var newComment = repalceData(ui, {
                id: message.comment_id,
                social_id: user.userID,
                social_type: user.social,
                childs: [],
                created: new Date(),
                comment: textareaComment.val(),
                name: user.name
              });

              textareaComment.val('');

              var hasFather = comment.find('input[name=parent_id]').length > 0;

              if (hasFather) {
                comment.replaceWith(newComment);
              } else {
                ui.commentsContainer.prepend(newComment);
              }
            })
            .fail(function (erro) {
              dialogAlert(alertBox, erro.responseJSON.message, "warning");
            })
        }
      } else {
        refreshLogin(ui);
        // commentButton.addClass('new_comment_needs_login');
        dialogAlert(alertBox, 'Realize Login', "info");

        /*
        setTimeout(function () {
          commentButton.removeClass('new_comment_needs_login')
        }, 1000);
        */

        setTimeout(function () {
          $('html, body').animate({
            scrollTop: socialIcons.offset().top - 30
          }, 500);

          socialIcons.addClass('new_comment_social_needs_login');

          setTimeout(function () {
            socialIcons.removeClass('new_comment_social_needs_login')
          }, 5000);
        }, 1500);
      }


    });

    $(document).on('click', '.comment_delete', function (e) {
      e.preventDefault();
      var commentNode = $(e.currentTarget);
      var commentId = commentNode.attr('data');
      var deleteContainer = commentNode.next();

      deleteContainer.toggle();
      commentNode.toggle();

    });

    $(document).on('click', '.comment_delete_confirm', function (e) {
      e.preventDefault();
      var commentNode = $(e.currentTarget).parent();
      var commentId = $(e.currentTarget).attr('data');
      $(e.currentTarget).html('Deletando...')

      deleteComment(deleteCommentForm, commentId)
        .done(function () {
          commentNode.parent().parent().remove();
        })
    })

    $(document).on('click', '.comment_delete_cancel', function (e) {
      e.preventDefault();
      var deleteContainer = $(e.currentTarget).parent();
      var commentNode = deleteContainer.prev();
      deleteContainer.toggle();
      commentNode.toggle();
    })

    $(document).on('click', '.comment_reply', function (e) {
      e.preventDefault();

      if (typeof replyComment !== "undefined") {
        $(replyComment).remove();
      }

      var commentNode = $(e.currentTarget);
      var commentId = commentNode.attr('data');

      replyComment = addCommentBox(ui, commentNode, commentId);
      $(replyComment).find('textarea')[0].focus();
    });

    $(document).on('click', '.new_comment_close', function (e) {
      e.preventDefault();
      jQuery(replyComment).fadeOut("fast");
    })

  });

})(jQuery)

/**
 * Intercepta a response para a função de parsing.
 *
 * @author Marcelo Henrique <marcelohenrique180@asav.org.br>
 * 
 * @param Promise requestPromise
 * @returns array
 */
function parseCommentsFromRequest(requestPromise) {
  return requestPromise
    .then(function (flatComments) { return parseComments(flatComments) })
}
