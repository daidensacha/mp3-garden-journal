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

//   $('.head-link').click(function(e) {
//     e.preventDefault();
    
//     var goto = $(this).attr('href');

//     $('html, body').animate({
//         scrollTop: $(goto).offset().top
//     }, 800);
// });

// $('.head-link').on('click', function (event) {
//     if (this.href !== '') {
//       event.preventDefault();
  
//       const hash = this.href;
  
//       $('html, body').animate({
//         scrollTop: $(hash).offset().top - 100
//       },
//         800
//       );
//     }
//   });

$(document).ready(function(){
    // Add smooth scrolling to all links
    $(".head-link").on('click', function(event) {
  
      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store hash
        var hash = this.hash;
  
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function(){
  
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        });
      } // End if
    });
  });
  