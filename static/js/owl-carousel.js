$(document).ready(function() {
    var x = window.matchMedia("(max-width: 991px)")

    if (x.matches) {
        $('#dr-finder').owlCarousel({
            autoplay: true,
            items: 3,
            margin: 340,
            loop: true,
            center: true
        })

        $('.owl-carousel').owlCarousel({
            loop: true,
            autoplay: false,
            center: true,
            items: 3,
        })
    } else {
        $('#dr-finder').owlCarousel({
            loop: true,
            autoplay: true,
            items: 3,
            margin: 50,
        })

        $('.owl-carousel').owlCarousel({
            loop: true,
            autoplay: true,
            center: true,
            items: 5,
            margin: 10,
        })
    }
});