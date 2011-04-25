$(document).ready(function() {
  $(".tip-able").tooltip({
    delay: 500,
    effect: 'fade',
    position: 'bottom center',
    events: {
      def: 'click, mouseout'
    }
  });

});
