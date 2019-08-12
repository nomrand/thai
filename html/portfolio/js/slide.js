const SLIDE_DURATION = 5000;
const SLIDE_IMAGE = [
    "img/test1.png",
    "img/test2.png",
    "img/test3.png",
    "img/test4.png",
];

$(function () {
    // initSlide();
    // slide();
});

function initSlide() {
    $('#subcont_table').css({
        top: $('#subcont_tr').height() + "px",
    });
}

let cur_slide = 0;
function slide() {
    cur_slide++;
    if (cur_slide >= SLIDE_IMAGE.length) {
        initSlide();
    }

    // IMAGES
    // Before Image fade out
    $('#subcont_tr td:first img').animate({
        opacity: 0,
    }, {
            duration: SLIDE_DURATION, easing: 'linear',
            complete: function () {
                this.remove();
            }
        });
    // After Image fade in
    let img = $("<img>");
    img.attr("src", SLIDE_IMAGE[cur_slide]);
    img.css({ "opacity": 0 });
    $('#subcont_tr td:first').append(img);
    img.animate({
        opacity: 1,
    }, {
            duration: SLIDE_DURATION, easing: 'linear',
            complete: function () {
                cur_slide++;
                if (cur_slide >= SLIDE_IMAGE.length) {
                    cur_slide = 0;
                }
            }
        });

    // TEXTS
    $('#subcont_table').animate({
        top: $("#subcont_table td").height(),
    }, {
            duration: SLIDE_DURATION, easing: 'linear',
            complete: function () {
                if (cur_slide >= SLIDE_IMAGE.length) {
                    cur_slide = 0;
                }
            }
        });
    setTimeout('slide()', SLIDE_DURATION);
}
