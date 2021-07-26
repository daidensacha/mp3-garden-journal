// (function($){
    $(function(){
  
        $('.sidenav').sidenav();
        $('.parallax').parallax();
        $('.slider').slider({
          full_width: false,
          interval:10000,
          transition:800,
        });
      //   $('.carousel').carousel({
          //   duration:200,
          //   padding:0,
          //   fullWidth: true,
      //   });
      //   autoplay();
      // function autoplay() {
      //     $('.carousel').carousel('next');
      //     setTimeout(autoplay, 4500);
      // }
      $('.materialboxed').materialbox();
      $('ul.tabs').tabs({
          // swipeable : true,
          // responsiveThreshold : 1920
      });
      $('.modal').modal();
    
      }); // end of document ready
  //   })(jQuery); // end of jQuery name space
  
  // Tabs fix for height issue as it is stykled by carousel css.
  $(function(){
      resizeTab();
      $( window ).resize(function() { resizeTab(); });
  });
  function resizeTab(){
      var maxHeight = 0;
      $('.carousel-item').each(function(){ 
           if($(this).height() > maxHeight) maxHeight = $(this).height(); 
      });
      $(".tabs-content").css('height',maxHeight+'px');
  }
  