$(document).ready(function() {
  $(".tip-able").tooltip({
    delay: 500,
    effect: 'fade',
    position: 'top center',
    events: {
      def: 'click, mouseout'
    }
  });

});
