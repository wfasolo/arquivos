(function ($) {

  $(document).ready(function () {

    var template = $("#twitter-button-template");
    
    $('.twitter-quote').each( function(i , element) {
      var classList = element.classList;
      element = $(element);
      var quote = element.html();
      var encodedQuote = encodeURI(quote);

      var content = template.html();

      var tweet = content
                    .replace('##TWEET', quote)
                    .replace('##EXTRA-CLASSES', classList.toString())
                    .replace('##TWEET_URL', encodedQuote);

      element.replaceWith(tweet);
    })

  })

})(jQuery)
