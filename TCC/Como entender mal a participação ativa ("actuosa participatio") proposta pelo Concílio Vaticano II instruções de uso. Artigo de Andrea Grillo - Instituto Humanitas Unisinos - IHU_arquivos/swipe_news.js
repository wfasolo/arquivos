/**
 * @package     Joomla.Site
 * @subpackage  Templates.ihu
 */




/**
 * jQuery.browser.mobile (http://detectmobilebrowser.com/)
 *
 * jQuery.browser.mobile will be true if the browser is a mobile device
 *
 **/

(function($)
{
    $(document).ready(function(){

        $(".prev-article").click(function(event) {
            event.preventDefault();
            prevArticle();
        });

        $(".next-article").click(function(event) {
            event.preventDefault();
            nextArticle();
        });

        // Verifica se o navegador é mobile
        if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
            $(".item-page").hammer({
                recognizers: [
                    [Hammer.Swipe, {
                        direction: Hammer.DIRECTION_HORIZONTAL
                    }],
                ]
            })
            .on("swipeleft", function(event) {
                // Próxima notícia
                nextArticle();
            })
            .on("swiperight", function(event) {
                // Notícia prévia
                prevArticle();
            });

            $(".next-article-arrows").css('display', 'none');
        }

    });

    function nextArticle() {
        url = $(".next-article").length > 0 ? $(".next-article").attr("href") : "";

        if ((typeof url !== undefined) && (url != "")) {
            changeArticle(url);
        }
    }

    function prevArticle() {
        url = $(".prev-article").length > 0 ? $(".prev-article").attr("href") : "";

        if ((typeof url !== undefined) && (url != "")) {
            changeArticle(url);
        }
    }

    function changeArticle(url) {
        window.location = url;
        //alert("Mudou para: " + url);
    }

})(jQuery);
