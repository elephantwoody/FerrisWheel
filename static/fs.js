var rotation = 0

setInterval(function() {
$('#wheel').css({
    "-moz-transform": "rotate(-" + rotation + "deg)",
    "-webkit-transform": "rotate(-" + rotation + "deg)",
    "-o-transform": "rotate(-" + rotation + "deg)",
    "-ms-transform": "rotate(-" + rotation + "deg)"
});

    $('.fa').css({
    "-moz-transform": "rotate(" + rotation + "deg)",
    "-webkit-transform": "rotate(" + rotation + "deg)",
    "-o-transform": "rotate(" + rotation + "deg)",
    "-ms-transform": "rotate(" + rotation + "deg)",
});

rotation = (rotation + 0.2) % 361
}, 50)
