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

  $('.modal').modal();
  $('select').formSelect();
  $('input.count-text, textarea.materialize-textarea').characterCounter();

  // Materialert customer alert for materialize css
  $(".materialert > .close-alert").click(function () {
    $(this).parent().hide('fade-out');
  });

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

// $(".materialert > .close-alert").click(function () {
//   $(this).parent().hide('fade-out');
// });

/*
Created by Josh Mason https://codepen.io/joshuamasen/pen/OYaYbL
*/

const scrollToTopButton = document.getElementById('js-top');

const scrollFunc = () => {

  let y = window.scrollY;

  if (y > 0) {
    scrollToTopButton.className = "top-link show";
  } else {
    scrollToTopButton.className = "top-link hide";
  }
};

window.addEventListener("scroll", scrollFunc);

const scrollToTop = () => {

  const c = document.documentElement.scrollTop || document.body.scrollTop;
  
  if (c > 0) {
    window.requestAnimationFrame(scrollToTop);

    window.scrollTo(0, c - c / 10);
  }
};

scrollToTopButton.onclick = function(e) {
  e.preventDefault();
  scrollToTop();
}

// Get event select add_category and add_plant url 
function handleSelect(redirect) {

  let dataAttr = redirect.options[redirect.selectedIndex].getAttribute('data-url');
  let url = window.location.origin;

  if (dataAttr) {
    window.location.href = url + dataAttr;
  }
  else return;
}
