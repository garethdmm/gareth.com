$(document).ready(function() {
  $(".tip-able").tooltip({
    delay: 500,
    effect: 'fade',
    position: 'center right',
    events: {
      def: 'click, mouseout'
    }
  });

});
