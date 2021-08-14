// (function($){
$(function () {
  $(".dropdown-trigger").dropdown({
    hover: true,
  });
  $('.sidenav').sidenav();
  $('.parallax').parallax();
  $('.slider').slider({
    indicators: false,
    full_width: false,
    interval: 10000,
    transition: 800,
  });
  $('.collapsible').collapsible({
    // accordion: false,
  });
  $('.tooltipped').tooltip();
  $('.datepicker').datepicker({
    format: "mmmm dd, yyyy",
    yearRange: 3,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  });
  $('.materialboxed').materialbox();
  $('ul.tabs').tabs({
    // swipeable : true,
    // responsiveThreshold : 1920
  });
  $('.modal').modal();
  $('select').formSelect();
// Materializecss select validation code from code institute walk through project. 
validateMaterializeSelect();
function validateMaterializeSelect() {
    let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
    let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
    if ($("select.validate").prop("required")) {
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}
}); // end of document ready
//   })(jQuery); // end of jQuery name space


// Tabs fix for height issue as it is stykled by carousel css.
$(function () {
  resizeTab();
  $(window).resize(function () {
    resizeTab();
  });
});

function resizeTab() {
  var maxHeight = 0;
  $('.carousel-item').each(function () {
    if ($(this).height() > maxHeight) maxHeight = $(this).height();
  });
  $(".tabs-content").css('height', maxHeight + 'px');
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

$(document).ready(function () {
  // Add smooth scrolling to all links
  $(".head-link").on('click', function (event) {

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
      }, 800, function () {

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});

$(".materialert > .close-alert").click(function () {
  $(this).parent().hide('fade-out');
});

