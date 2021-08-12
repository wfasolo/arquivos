/**
 * 
 * 
 * @param {Jquery object} alert
 * @param {String} message
 * @param {String} type sucess or warning
 */
function dialogAlert(alert, message, type) {
  alert.html(message);
  
  alert.removeAttr("style")
  alert.removeClass('alert_box_success');
  alert.removeClass('alert_box_warning');
  alert.removeClass('alert_box_info');

  switch (type) {
    case 'success':
      alert.addClass('alert_box_success');
      break;

    case 'warning':
      alert.addClass('alert_box_warning');
      break;

    case 'info':
      alert.addClass('alert_box_info');
      break;
  
    default:
      break;
  }

  setTimeout(function() {
    alert.fadeOut("slow", function() {
      alert.removeAttr("style")
      alert.removeClass('alert_box_success');
      alert.removeClass('alert_box_warning');
      alert.removeClass('alert_box_info');
    });
  }, 4000);
}