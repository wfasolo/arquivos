jQuery(document).ready(function(){
    //Click on close button
    jQuery('.reportError_close').click(function() {
        var parent = jQuery(this).parents().eq(3);
        parent.find(".reportError_modal").fadeToggle();
        parent.find(".reportError_modal").css({"display" : "none"});
        jQuery("body").removeClass("body-overlayed");
        jQuery(".reportError_return").hide();
        jQuery("#formularioReportError").show();
        cleanFields();
    });

    jQuery('.reportError_button').click(function() {
        jQuery(".bg-reportError").fadeToggle();
        jQuery(".bg-reportError").css({"display" : "block"});
        var parent = jQuery(this).parents().eq(1);
        parent.find(".reportError_modal").fadeToggle();
        parent.find(".reportError_modal").css({"display" : "block"});
        jQuery("body").addClass("body-overlayed");
    });

    jQuery("#e_mail").blur(function(){
        emailValidate("e_mail","","border: 1px solid #FF0000");
    });

    jQuery(document).on('submit', '#formularioReportError', function (event) {
        event.preventDefault();
        // return false
    });

    jQuery( document ).on( "click",".form_button",function(){
       sendData();
    });

    function validationOfFields(){

        var nome       = jQuery("#name");
        var email      = jQuery("#e_mail");
        var descricao  = jQuery("#description");
        var error      = false;

        if( nome.val().trim().length == 0 ){
            nome.addClass("fieldsWithError");
            error = true;
        }else{
            nome.removeClass("fieldsWithError");
        }


        if( email.val().trim().length != 0  ){
            if(!emailValidate("e_mail","","border: 1px solid #FF0000"))
                error = true;
            else
                email.removeClass("fieldsWithError");
        }else{
            email.addClass("fieldsWithError");
            error = true;
        }

        if( descricao.val().trim().length == 0 ){
            descricao.addClass("fieldsWithError");
            error = true;
        }else{
            descricao.removeClass("fieldsWithError");
        }

        return error;
    }

    function sendData(){
        if(!validationOfFields()){
            showLoad();
            jQuery(".reportError_return").empty();
            jQuery.ajax({
                url: "?option=com_ajax&module=asavreporterror&method=sendEmail&format=json",
                type: "POST",
                data: {
                    urlNoticia: window.location.href,
                    nome: jQuery("#name").val().trim(),
                    email: jQuery("#e_mail").val().trim(),
                    descricao: jQuery("#description").val().trim(),
                    recaptcha: jQuery('[name="g-recaptcha-response"]').val(),
                },
                dataTypes: "JSON",
                success: function(result) {
                    switch (result.data.codigo){
                        // success
                        case "0":
                            success(jQuery.parseJSON(result.data.texto));
                            break;

                        // error
                        case "1":
                            error(jQuery.parseJSON(result.data.texto));
                            break;

                        // information
                        case "2":
                            information(jQuery.parseJSON(result.data.texto));
                            validationOfFields();
                            break;
                    }
                },
                complete: function(result){
                    hideLoad();
                }
            });
        }
    }

    function emailValidate( campo, style, styleErro ) {
        var id = jQuery( '#' + campo );
        cod = (campo).substring((campo).length-7,(campo).length);
        var er = /^[a-zA-Z0-9][a-zA-Z0-9\._-]+@([a-zA-Z0-9\._-]+\.)[a-zA-Z-0-9]{2,3}/;
        if( id.val() !== '' && !er.exec( id.val() ) ) {
            id.attr( 'style', styleErro );
            return false;
        } else {
            id.attr( 'style', style );
            return true;
        }
    }

    function success(mensagem){
        html = "";
        html += "<i class='fa fa-check' aria-hidden='true'/>";
        html += mensagem;
        jQuery(".reportError_return").empty();
        jQuery(".reportError_return").append(html);
        jQuery(".reportError_return i").css("color","#5CB85C");
        jQuery(".reportError_return").css("padding", "40px 0");
        jQuery(".reportError_return").show();
        jQuery("#formularioReportError").hide();
        cleanFields();
    }

    function error(mensagem) {
        html = "";
        html += "<i class='fa fa-times' aria-hidden='true'/>";
        html += mensagem;
        jQuery(".reportError_return").empty();
        jQuery(".reportError_return").append(html);
        jQuery(".reportError_return i ").css("color","#D05A15");
        jQuery(".reportError_return").css("padding", "40px 0");
        jQuery(".reportError_return").show();
        jQuery("#formularioReportError").hide();
        cleanFields();
    }

    function information(mensagem){
        html = "";
        html += "<i class='fa fa-exclamation-triangle' aria-hidden='true'/>";
        html += mensagem;
        jQuery(".reportError_return").empty();
        jQuery(".reportError_return").append(html);
        jQuery(".reportError_return i ").css("color","#fc6b01");
        jQuery(".reportError_return").css("padding", "0px");
        jQuery(".reportError_return").show();
        jQuery("#formularioReportError").show();
    }

    function cleanFields(){
        //limpando os campos
        jQuery("#name").val("");
        jQuery("#e_mail").val("");
        jQuery("#description").val("");

        //retirando a borda dos campos
        jQuery("#name").removeClass("fieldsWithError");
        jQuery("#e_mail").removeClass("fieldsWithError");
        jQuery("#e_mail").css("border","");
        jQuery("#description").removeClass("fieldsWithError");
        hideLoad();
        grecaptcha.reset();
    }

    function showLoad(){
        jQuery(".load").show();
        jQuery("#formularioReportError").hide();
    }

    function hideLoad(){
        jQuery(".load").hide();
    }


});