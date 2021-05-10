/**
 * @package     Joomla.Site
 * @subpackage  Templates.ihu
 */

(function($)
{
    $(document).ready(function(){

        $(".topmenu .parent").click(function() {
            // Remove a classse ativa dos irmãos e escode os sobrinhos
            $(this)
                .siblings(".active")
                .removeClass("active")
                .find(".nav-child")
                .hide();

            var menuChild = $(this).find(".nav-child");

            if($(menuChild).is(":visible")) {
                $(menuChild).parent().removeClass("active");
                $(".topmenu .current").addClass("active");
            } else {
                $(".topmenu .current").removeClass("active");
                $(this).addClass("active");
            }

            $(this).find(".nav-child").slideToggle("slow");

        });

        //Check dos botões da página BUSCA
        $("label.radio").click(function(){
            $("label.radio").removeClass("checked");
            $(this).addClass("checked");
        });

        //Click do menu no RESPONSIVO
        $(".close-nav-button").click(function(){
            $(".open-mobile-menu").animate({height:'toggle'}, 300);

        });

        $(".mobile-menu-button").click(function(){
            $(".open-mobile-menu").animate({height:'toggle'}, 300);

        });

        //Click do calendario em eventos
        $(".calendar-button").click(function() {
            $(".calendar-box").slideToggle();
        });

        //Click do News Font
        $('.fa-font').click(function(){
            var normal = Number($('.news-body-content').css('font-size').split('px').join(''))

            if($(this).attr('data-num') == 'mais' && normal < 20){
                var valor = normal += 1;
            }else{ 
                if($(this).attr('data-num') == 'menos' && normal > 14){
                    var valor = normal -= 1;
                }else{
                    var valor = normal;
                }
            }

            $('.news-body-content').css('font-size', valor+'px');
        });

        var $m = jQuery.noConflict();

        $m( window ).scroll(function() {
            if ($m(this).scrollTop() > 275) {
                $m(".next-article-arrows-left").addClass('next-article-arrows-fixo-left');
                $m(".next-article-arrows-right").addClass('next-article-arrows-fixo-right');
            }else{
                $m(".next-article-arrows-left").removeClass('next-article-arrows-fixo-left');
                $m(".next-article-arrows-right").removeClass('next-article-arrows-fixo-right');
            };
        });
    });

})(jQuery);
