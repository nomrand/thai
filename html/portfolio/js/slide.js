const SLIDE_DURATION = 5000;
const SLIDE_IMAGE = [
    "img/test1.png",
    "img/test2.png",
    "img/test3.png",
    "img/test4.png",
];

$(function(){
    slide();
});

let cur_slide = 0;
function slide() {
    cur_slide++;

    // IMAGES
    $('#subcont_tr td:first img').animate({
        opacity: 0,
    }, { duration: SLIDE_DURATION, easing: 'linear',
        complete: function(){
            this.remove();
        }
    });
    let img = $("<img>");
    img.attr("src", SLIDE_IMAGE[cur_slide]);
    img.css({"opacity": 0});
    $('#subcont_tr td:first').append(img);
    img.animate({
        opacity: 1,
    }, { duration: SLIDE_DURATION, easing: 'linear', });

    // TEXTS
    $('#subcont_table').animate({
        top: (cur_slide * $("#subcont_table td").height()) + 'px'
    }, { duration: SLIDE_DURATION, easing: 'linear', });
    setTimeout('slide()', SLIDE_DURATION);
}
